# Diagnóstico y mediciones para algoritmos de ML de clasificación

Supongamos un investigador/ingeniero ML llamado Ignasio en una empresa ficticia llamada la "Empresa Feliz". Ignasio tiene la tarea de entrenar un modelo que clasifique correctamente transacciones como fraudulentas o legítimas.

Para ello se le suministran permisos de acceso en base de datos para consultar transacciones historicas. Ignasio está feliz porque usó pytorch para crear su MLP con el módulo `n.n`, sin embargo después de un entrenamiento de varios días con su pc encendido consumiendo electricidad con su RTX 5070 viene una pregunta muy importante y fundamental: **¿Esto si está aprendiendo al clasificar?**

Específicamente, los algoritmos de clasificación como los MLP, random forest, SVM etc tiene una clara función y es que basado en los datos de entrenamiento, los "engranajes internos" del algoritmo se acomodan para **generalizar** los datos, y ante uno nuevo totalmente desconocido es capaz de reconocer los patrones y decir a qué categoría es propable que pertenezca

Por lo cual, lo que sigue son los conceptos fundamentales y mas importantes para concluir si Ignasio está haciendo bien su trabajo y no será despedido de la Empresa Feliz

## Parte 1 — Los cimientos

### 1.1 ¿Qué significa "generalizar"?

En la "Escuela Feliz" dos estudiantes de octavo grado cursan por primera vez álgebra 1, una materia que suele ser retadora para todos los estudiantes. El estudiante A tiene la costumbre de aprenderse de memoria todos los ejercicios que el profesor propone, mientras que el estudiante W intenta entender el por qué de todos los procesos y trucos aritméticos que se enseñan en la clase

El día del examen del primer corte el profesor usa preguntas de talleres que envió a los estudiantes durante las semanas previas al examen. En este caso, ambos el estudiante A y W aprueban con una nota alta. Sin embargo, para el segundo corte el profesor decide usar algunas preguntas nuevas que ningún estudiante ha visto, pero que conservan el espíritu y los mecanismos de otros ejemplos compartido en los talleres

Podemos imaginar el resultado, cuando el estudiante A ve las preguntas nuevas no puede resolverlas y repureba el examen. El estudiante W entiende el por qué de todo y logra responder la mayoría bien, aprobando.

Vale la pena mencionar que si el profesor evaluara cálculo integral en vez de álgebra, ni siquiera W aprobaría, y no sería justo llamarlo "mala generalización".

---
Usando la terminología técnica, existe una **real distribution** (distribución real) de problemas de álgebra —llamémosla *D*— que contiene todos los ejercicios posibles del universo del álgebra 1, tanto los que ya se resolvieron en clase como los que jamás se han planteado. Ni el estudiante A ni el estudiante W tienen acceso a *D* completa; lo único que vieron fueron los talleres de las semanas previas, es decir, un **sample** (muestra finita) de esa distribución que llamaremos *S*.

Cuando el estudiante A se aprende de memoria los ejercicios de los talleres, está minimizando su error sobre *S*, sobre la muestra que sí tuvo enfrente. A eso se le llama **empirical risk** (riesgo empírico): qué tan seguido se equivoca en los ejemplos que ya conoce. Y por eso en el primer corte le va bien, porque el profesor evaluó justamente con preguntas sacadas de *S*.

Pero lo que de verdad mide si alguien aprendió álgebra no es *S*, sino *D*: la capacidad de responder cualquier ejercicio del universo entero, incluidos los que nunca vio. Ese es el **true risk** (riesgo verdadero), el error sobre toda la distribución. El estudiante W lo tiene bajo porque entendió los mecanismos de fondo; el estudiante A lo tiene por las nubes, aunque su empirical risk fuera casi cero.

**Generalizar es lograr que el true risk sea bajo, y no solo el empirical risk.** El segundo corte —con preguntas nuevas que conservan el espíritu de los talleres— es precisamente un intento del profesor de estimar el true risk: tomar una segunda muestra que el estudiante no vio y usarla para descubrir quién entendió y quién solo memorizó. Ese es, exactamente, el papel que van a cumplir los **test data** (datos de prueba) con el modelo de Ignasio.


### 1.2 El objeto que medimos es un *score*, no una decisión

Recordando la regresión logística: el modelo nunca dice directamente "esto es fraude". Lo que hace es ajustar una recta y aplanarla con la sigmoide para obtener un número entre 0 y 1 (un **score**), que interpretamos como "qué tan probable es que este ejemplo sea fraude". La decisión ("es fraude" / "no es fraude") es un paso aparte, se obtiene comparando ese score contra un umbral, típicamente `0.5`.

Ahí está el punto clave, el modelo no produce una decisión sino un **score**, y la decisión es algo que nosotros le imponemos después. Si evaluamos a Ignasio mirando solo la decisión final, perdemos información. Un ejemplo con score `0.51` y otro con `0.9` caen del mismo lado del umbral (a ambos el modelo los llama "fraude") pero el segundo lo dice con muchísima más **confianza** que el primero. Si solo miramos la etiqueta final, esa diferencia desaparece, y esa diferencia es justo lo que nos dice si el modelo entendió el problema o apenas está **adivinando** cerca del borde.

Por eso, antes de hablar de umbrales y decisiones, conviene evaluar el score en sí mismo. El score tiene dos cualidades que son totalmente independientes entre sí:

- **Ordenar bien**: ¿el modelo tiende a darles score más alto a los fraudes de verdad que a las transacciones legítimas? No importa el valor exacto que le ponga a cada ejemplo, importa que el orden relativo sea el correcto. Un modelo que le da `0.05` a los fraudes y `0.02` a las transacciones legítimas ordena perfecto, aunque ningún score individual "parezca" alto.
- **Que el número sea una probabilidad creíble**: si el modelo dice `0.8`, ¿de verdad, entre todos los casos donde dijo algo cercano a `0.8`, alrededor de 8 de cada 10 resultan ser fraude? Un modelo puede ordenar perfecto y aun así estar mal calibrado — por ejemplo, si sistemáticamente dice `0.95` cuando la tasa real ronda el 60%.


#### Ejemplo 1 — Ordenar bien

**La pregunta:** ¿el modelo les da score más alto a los fraudes reales que a las transacciones legítimas? No importa el valor exacto, importa el orden relativo.

Tomemos 6 transacciones que ya sabemos qué eran de verdad, y dos modelos que les asignan scores distintos:

| transacción | real     | Modelo A | Modelo B |
|-------------|----------|----------|----------|
| t1          | Fraude   | 0.90     | 0.09     |
| t2          | Fraude   | 0.85     | 0.085    |
| t3          | Fraude   | 0.70     | 0.07     |
| t4          | Legítima | 0.30     | 0.03     |
| t5          | Legítima | 0.20     | 0.02     |
| t6          | Legítima | 0.10     | 0.01     |

Los dos modelos **ordenan idéntico**: los tres fraudes quedan por encima de las tres legítimas, sin ni un solo cruce. Si armáramos una cola de revisión "de más sospechoso a menos sospechoso", ambos producen exactamente la misma lista. Su AUC sería el mismo (1.0, separación perfecta).

Y sin embargo el **Modelo B nunca dice un número que "parezca" fraude**: su score más alto es `0.09`. A un ojo humano le grita "acá no hay nada", pero el orden relativo es perfecto.

> **La idea:** ordenar bien no depende de la magnitud, depende de quién queda arriba de quién. Un fraude con `0.09` y una legítima con `0.01` está perfectamente ordenado, aunque ningún número supere el `0.5` de rigor.

Esto es lo que miden **ROC / AUC** y **PR / AP**.

#### Ejemplo 2 — Que el número sea una probabilidad creíble (calibración)

**La pregunta:** cuando el modelo dice `0.8`, ¿de verdad, entre todos los casos donde dijo algo cercano a `0.8`, alrededor de 8 de cada 10 resultan ser fraude?

El modelo "dice 80%" en el instante en que le asigna el score `0.8` a una transacción — es lo mismo dicho de dos maneras. Verificar si ese `0.8` era honesto es un paso posterior: juntar todos los casos donde dijo `0.8` y ver qué pasó de verdad.

##### Un solo nivel (el 0.8)

Ignasio junta las 10 transacciones donde el modelo dijo algo cercano a `0.8`:

- **Caso calibrado:** de esas 10, resultaron fraude 8. El modelo dijo "80%" y el 80% real era fraude. El número es creíble.
- **Caso mal calibrado (sobreconfiado):** de esas 10, resultaron fraude solo 6. El modelo dice `0.8` pero la tasa real ronda el 60%. El número existe igual, pero miente.

##### Todos los niveles a la vez (reliability diagram)

Lo mismo se hace para todo el rango de scores, no solo el 0.8. Como los scores son continuos (`0.8017`, `0.7994`...), no se agrupa por valor exacto sino por **rangos (baldes)**. Para cada balde se compara lo que el modelo promete contra lo que pasó de verdad:

| balde de score | qué junta       | modelo dice (promedio) | pasó de verdad          |
|----------------|-----------------|------------------------|-------------------------|
| [0.0, 0.2)     | los de score bajo | ~0.10                | ¿qué fracción fue fraude? |
| [0.2, 0.4)     | los del 20-30%  | ~0.30                  | ¿qué fracción fue fraude? |
| [0.4, 0.6)     | los del medio   | ~0.50                  | ¿qué fracción fue fraude? |
| [0.6, 0.8)     | los altos       | ~0.70                  | ¿qué fracción fue fraude? |
| [0.8, 1.0]     | los muy altos   | ~0.90                  | ¿qué fracción fue fraude? |

Un modelo bien calibrado tiene, en **cada** balde, "lo que dice" ≈ "lo que pasó". No solo en el del 0.8 — en todos.

> **Analogía:** un pronosticador que dice "80% de lluvia" ya lo dijo en ese momento. Que sea bueno se sabe después, juntando todos los días que dijo "80%" y viendo si llovió en 8 de cada 10. El modelo es el pronosticador; el score es el "80%"; la calibración es revisar su historial.

Esto es lo que miden el **reliability diagram**, el **ECE** y el **Brier score**.

##### Lo clave: son independientes

- El **Modelo B** del ejemplo 1 ordena impecable, pero sus números (`0.09`, `0.01`) son ridículamente bajos → buena discriminación, mala calibración.
- Un modelo **sobreconfiado** puede ordenar perfecto y aun así inflar los números (`0.8` cuando es 60%) → buena discriminación, mala calibración.
- Un modelo que le asigna a **todo** la prevalencia (ej. `0.4` a todas) está bien calibrado en el agregado pero no distingue nada → mala discriminación, buena calibración.

Por eso se miden con herramientas distintas: **ROC/AUC y PR/AP** para el orden, **reliability diagram, ECE y Brier** para la credibilidad del número.


Son independientes porque un modelo puede tener una de las dos sin la otra: puede ordenar de maravilla mientras sus números están sistemáticamente desviados, o puede tener números creíbles en promedio pero un orden mediocre. Vamos a volver a esta distinción más adelante — ordenar bien es lo que miden ROC y PR-AUC (Parte 3), y que el número sea creíble es lo que mide la calibración (Parte 4).


### 1.3 La matriz de confusión: TP, FP, FN, TN

Ya vimos que el score se convierte en decisión al compararlo contra un umbral. Una vez Ignasio tiene esa decisión para cada transacción, puede cruzarla contra la verdad (lo que la transacción *realmente* era) y le salen cuatro casos posibles:

| | Real: Fraude | Real: Legítima |
|---|---|---|
| **Predicho: Fraude** | True Positive (TP) | False Positive (FP) |
| **Predicho: Legítima** | False Negative (FN) | True Negative (TN) |

- **True Positive (TP)**: era fraude, el modelo dijo fraude. Acierto — el fraude queda atrapado.
- **True Negative (TN)**: era legítima, el modelo dijo legítima. Acierto — a un cliente honesto no lo molestan.
- **False Positive (FP)**: era legítima, pero el modelo dijo fraude. Falsa alarma — a un cliente honesto le bloquean la tarjeta sin razón.
- **False Negative (FN)**: era fraude, pero el modelo dijo legítima. El peor caso para la Empresa Feliz — el fraude pasa como si nada.

Esta matriz es la materia prima de casi todo lo que viene: precision, recall, F1 y accuracy (Parte 2) no son más que distintas formas de combinar estos cuatro números. Pero ojo — la matriz completa depende de un umbral fijo. Si Ignasio mueve el umbral, algunos TP se le vuelven FN, algunos TN se le vuelven FP, y la matriz cambia entera. De eso trata la siguiente sección.

### 1.4 El umbral de decisión

Ya vimos que el score y la decisión son cosas distintas, y que la decisión sale de comparar el score contra un umbral. Lo que falta aclarar es qué tan arbitrario es ese umbral. El `0.5` es apenas la convención por defecto, el umbral es puro post-proceso, tan fácil de cambiar como una línea de código

Y al moverlo la matriz de confusión entera cambia con él. Supongamos que Ignasio corrió el modelo sobre 20 transacciones de validación. Estas ocho eran fraude de verdad, con estos scores:

`0.93, 0.85, 0.79, 0.70, 0.62, 0.54, 0.47, 0.36`

Y estas doce eran legítimas de verdad:

`0.66, 0.58, 0.50, 0.43, 0.37, 0.31, 0.26, 0.20, 0.15, 0.10, 0.06, 0.02`

Fijate que los dos grupos se solapan: hay transacciones legítimas con score más alto (`0.66`) que transacciones fraudulentas (`0.36`). Eso es lo normal — un modelo real casi nunca separa las dos clases con una frontera limpia, y es justo lo que hace que la posición del umbral importe.

Con umbral `0.5`, cruzan la línea seis fraudes reales (de `0.93` a `0.54`) — esos son **TP** — y quedan del otro lado dos (`0.47` y `0.36`) — esos son **FN**. De las legítimas, cruzan tres (`0.66`, `0.58`, `0.50`) — **FP** — y las nueve restantes son **TN**. Resultado: 6 TP, 3 FP, 2 FN, 9 TN.

Si Ignasio baja el umbral a `0.35`, hasta el fraude más débil (`0.36`) cruza la línea: los ocho fraudes reales quedan atrapados, 0 FN. Pero también cruzan cinco legítimas más (`0.66` a `0.37`). La matriz pasa a 8 TP, 5 FP, 0 FN, 7 TN — atrapó todo el fraude, a costa de más falsas alarmas.

Si en cambio lo sube a `0.65`, dejan de cruzar la línea cuatro fraudes reales (`0.62`, `0.54`, `0.47`, `0.36`), que se vuelven **FN**. Solo una legítima (`0.66`) sigue marcada como FP. La matriz pasa a 4 TP, 1 FP, 4 FN, 11 TN — casi no genera falsas alarmas, pero ahora se le escapa la mitad del fraude real.

Ningún score cambió entre los tres escenarios. Es el mismo modelo, la misma tabla de 20 transacciones. Lo único que se movió fue la perilla, y eso alcanzó para reacomodar TP, FP, FN y TN por completo. Por eso no tiene sentido decir "mi modelo tiene 90% de precision" sin aclarar a qué umbral — y podés reproducir este mismo recorrido moviendo el umbral en el simulador interactivo de esta sección.

> Simulador interactivo: [html/score_umbral_metricas_prevalencia.html](html/score_umbral_metricas_prevalencia.html). Cubre desde el riesgo empírico vs verdadero (1.1) hasta la prevalencia (2.5): un slider mueve el umbral sobre las mismas 20 transacciones y recalcula en vivo la matriz de confusión, precision, recall, F1 y accuracy; otro slider mueve la prevalencia y muestra cómo se derrumba precision al pasar de validación a producción.

¿Y quién decide dónde poner la perilla? prácticamente el negocio. Bajar el umbral favorece recall (atrapar más fraude) a costa de molestar más clientes honestos; subirlo favorece precision (menos falsas alarmas) a costa de dejar pasar más fraude. Cuál de los dos errores le sale más caro a la Empresa Feliz es exactamente el tema de la Parte 6 (matriz de costos, selección de umbral). Por ahora, lo importante es entender que el umbral es una decisión aparte del modelo, no una propiedad suya.

## Parte 2 — Métricas a UN umbral fijo (un punto)

### 2.1 Precision

Retomemos la matriz de confusión de la sección 1.4. Con umbral `0.5`, Ignasio tenía 6 TP, 3 FP, 2 FN y 9 TN. La pregunta que responde **precision** es puntual: de todas las veces que el modelo gritó "¡fraude!", ¿cuántas veces tenía razón?

```
precision = TP / (TP + FP)
```

En el ejemplo, el modelo marcó "fraude" nueve veces (6 TP + 3 FP) y acertó en seis: precision = 6/9 ≈ 0.67. Dicho en criollo, dos de cada tres alarmas son reales; la tercera es un cliente honesto al que le bloquearon la tarjeta sin motivo.

Precision solo mira la fila "Predicho: Fraude" de la matriz. Le da igual cuántos fraudes reales existen en total o cuántos se le escaparon al modelo — eso es asunto del recall, que viene en la siguiente sección. Precision contesta una pregunta distinta: cuando el modelo actúa, ¿qué tan confiable es esa acción?

Por qué le importa a la Empresa Feliz: cada FP es un cliente real al que le rechazan la compra, que llama a soporte enojado y que quizás se cambia de banco. Si precision es baja, la alarma del modelo deja de ser creíble — tanto para los clientes como para el equipo humano que revisa cada caso marcado. Con suficiente volumen de transacciones, un precision bajo puede enterrar a ese equipo en falsas alarmas.

Vale la pena notar un caso extremo: un modelo tramposo que casi nunca dice "fraude" — solo en el único caso donde está segurísimo — puede lograr precision de 1.0 sin atrapar casi ningún fraude real. Precision alta no significa "atrapa mucho fraude"; significa "cuando actúa, no se equivoca". Que tan seguido actúa (y qué tanto fraude real atrapa) es justo lo que mide recall.

### 2.2 Recall

Si precision mira la fila "Predicho: Fraude", **recall** mira la columna "Real: Fraude". La pregunta cambia de bando: de todos los fraudes que de verdad ocurrieron, ¿cuántos atrapó el modelo?

```
recall = TP / (TP + FN)
```

Con el umbral `0.5` del ejemplo de 1.4, Ignasio tenía 6 TP y 2 FN: recall = 6/8 = 0.75. Atrapó tres de cada cuatro fraudes reales; se le escaparon los dos con score más bajo entre los fraudes (`0.47` y `0.36`), que no llegaron a cruzar la línea. Precision, en ese mismo punto, era 0.67 — un número parecido pero no igual, la primera pista de que ambas métricas miden cosas distintas, aunque acá no estén en extremos opuestos.

Ahora recordemos qué pasaba si Ignasio subía el umbral a `0.65` (también en 1.4): la matriz cambiaba a 4 TP, 1 FP, 4 FN, 11 TN. Los fraudes con score `0.62`, `0.54`, `0.47` y `0.36` dejaron de cruzar la línea y se volvieron FN. recall = 4/8 = 0.5. De un plumazo, subir la perilla para ganar precision (subió de 0.67 a 0.8) le costó la mitad del recall: ahora se le escapa uno de cada dos fraudes reales.

Recall le da igual cuántas falsas alarmas genera el modelo; solo le importa no dejar pasar fraude real. Por eso a veces se le llama **sensitivity** o **true positive rate** — es la misma cantidad con otro nombre, y va a reaparecer en la Parte 3 cuando hablemos de la curva ROC.

Por qué le importa a la Empresa Feliz: cada FN es un fraude que pasó como transacción normal — plata que se pierde, y potencialmente un cliente que descubre después que le robaron y culpa al banco por no haberlo detectado. Si el costo de un fraude no detectado es mucho mayor que el costo de molestar a un cliente honesto (algo muy plausible en fraude financiero), Ignasio va a querer un recall alto aunque eso le cueste precision — y de ahí sale, otra vez, la pregunta del umbral correcto que retomamos en la Parte 6.

Igual que con precision, hay un caso extremo que conviene tener en mente: un modelo tramposo que marca *todas* las transacciones como fraude logra recall de 1.0 perfecto — nunca deja pasar un fraude real, porque nunca deja pasar nada. Por supuesto, su precision sería pésima (bombardeando a todo cliente honesto con falsas alarmas). Ningún extremo sirve solo: se necesita ambas métricas a la vez, y de esa tensión trata la siguiente sección.

### La tensión precision–recall   (por qué no podés maximizar las dos)

Ya se asomó en las dos secciones anteriores: al mover el umbral de 0.5 a 0.65, Ignasio ganó precision (de 0.67 a 0.8) pero perdió recall (de 0.75 a 0.5). No fue mala suerte con ese ejemplo puntual — es estructural, y vale la pena entender por qué.

Pensemos en la perilla del umbral (1.4) barriendo desde 0 hasta 1, sobre las mismas 20 transacciones de Ignasio. En el extremo `umbral = 0`, el modelo marca las 20 como fraude: recall = 8/8 = 1.0 (ningún fraude se le escapa, porque nada se le escapa) pero precision cae a 8/20 = 0.4 — exactamente la proporción de fraude real en los datos (el base rate, tema de la próxima sección). En el extremo opuesto, `umbral = 1` (más alto que cualquier score observado), el modelo no marca nada como fraude: 0 FP, así que precision queda indefinida (0/0, nunca dijo "fraude"), pero recall se derrumba a 0/8 = 0.

Entre esos dos extremos, cada vez que Ignasio sube el umbral un poquito, algún caso que antes cruzaba la línea deja de cruzarla. Ese caso era, antes del movimiento, o un TP o un FP (era algo que el modelo marcaba "fraude"). Si era un FP, al sacarlo la precision sube. Si era un TP, al sacarlo se convierte en FN y el recall baja. En la práctica los scores están mezclados — ni todos los casos que se caen al subir el umbral son FP, ni todos son TP —, y por eso lo típico es que subir el umbral mueva ambas cosas a la vez: sube la precision (se eliminan más FP de los que se convierten TP→FN) y baja el recall (los TP que se pierden). Bajar el umbral hace exactamente lo simétrico.

Esto no es una limitación de Ignasio ni de su modelo en particular: es geométrico. TP y FP viven del mismo lado de la línea (el lado "predicho fraude"), así que cualquier movimiento de la línea los afecta a los dos juntos. No existe un umbral mágico que maximice precision y recall simultáneamente, salvo en el caso irreal de un clasificador perfecto que separe las dos clases sin ningún solapamiento de scores.

Por eso "mi modelo tiene 95% de precision" y "mi modelo tiene 95% de recall" son afirmaciones incompletas si no se dice a qué umbral, y por eso comparar dos modelos mirando solo una de las dos métricas es tramposo: alguien pudo simplemente mover la perilla. Lo que hace falta es una forma de resumir el compromiso entre ambas en un solo número (F1, siguiente sección) o, mejor todavía, una forma de comparar modelos sin comprometerse a ningún umbral en particular (la curva PR de la Parte 3).

### F1   (y por qué media armónica y no promedio normal)

Ignasio quiere reportarle un solo número a su jefe, no un par de números que se mueven en direcciones opuestas cada vez que toca la perilla del umbral. La tentación obvia es promediarlos: `(precision + recall) / 2`. Esa tentación es una trampa, y vale la pena ver por qué con números.

Imaginemos un modelo tramposo — el mismo del final de 2.2 — que marca *todas* las transacciones como fraude. Ya vimos que recall = 1.0 (nunca deja pasar un fraude real) pero precision es pésima: si el 1% de las transacciones son fraude, precision ronda 0.01. El promedio normal (**media aritmética**) de estos dos números es `(0.01 + 1.0) / 2 = 0.505`. Un 50% suena a "más o menos aceptable" — y es completamente falso, porque ese modelo es inútil: bloquea a todo el mundo.

El problema de la media aritmética es que un número alto puede "tapar" a uno bajo. Para que el resumen sea honesto, hace falta una media que castigue fuerte cuando cualquiera de los dos valores es malo, no que los deje compensarse. Esa es la **media armónica**, y así se define **F1**:

```
F1 = 2 · (precision · recall) / (precision + recall)
```

Con el ejemplo del modelo tramposo: `F1 = 2 · (0.01 · 1.0) / (0.01 + 1.0) ≈ 0.0198`. Ahí sí queda claro que el modelo es malo — la media armónica se acerca mucho al valor más bajo de los dos, no al promedio. Es matemáticamente así porque la media armónica es dominada por el término más pequeño (si un denominador se dispara porque uno de los valores es chiquito, todo el resultado se hunde). En cambio, cuando precision y recall son parecidos entre sí, F1 se acerca bastante a la media aritmética — la diferencia solo se nota (y solo importa) cuando uno de los dos está cojo.

Con los números reales de Ignasio a umbral `0.5` (precision ≈ 0.67, recall = 0.75): `F1 = 2 · (0.67 · 0.75) / (0.67 + 0.75) ≈ 0.706`. Un número honesto, entre los dos, ni tan optimista como recall solo ni tan pesimista como precision sola.

Dos advertencias para no usar F1 en piloto automático:

- F1 sigue siendo una métrica **a un umbral fijo** — hereda todo el problema de la sección 1.4. Cambiar el umbral cambia precision y recall, y por lo tanto cambia F1. "Mi modelo tiene F1 de 0.8" sigue siendo incompleto sin decir a qué umbral.
- F1 le da el mismo peso a precision y a recall, como si a la Empresa Feliz le doliera igual un FP que un FN. Casi nunca es así (ver Parte 6, matriz de costos) — cuando un tipo de error pesa más que el otro, existe **F-beta**, una variante de F1 que pondera uno de los dos más que el otro. No entramos en el detalle acá, pero conviene saber que F1 es un caso particular (el balanceado) de una familia más amplia.

### Accuracy y por qué miente con clases desbalanceadas

Antes de meternos con precision, recall y F1, la métrica más obvia que a cualquiera se le ocurre es **accuracy**: ¿qué fracción de todas las predicciones fueron correctas?

```
accuracy = (TP + TN) / (TP + FP + FN + TN)
```

Con la matriz de umbral `0.5` de 1.4 (6 TP, 3 FP, 2 FN, 9 TN): accuracy = 15/20 = 0.75. Suena razonable. Pero mirá lo que pasa si repetimos la cuenta en los otros dos umbrales que recorrimos en 1.4 y 2.2: a `0.35` (8 TP, 5 FP, 0 FN, 7 TN) accuracy también da 15/20 = 0.75, y a `0.65` (4 TP, 1 FP, 4 FN, 11 TN) vuelve a dar 15/20 = 0.75. Tres umbrales distintos, con precision moviéndose de 0.62 a 0.8 y recall derrumbándose de 1.0 a 0.5 — y accuracy, completamente ciego a ese vaivén, clavado en el mismo número los tres veces. Eso ya es una señal de alerta sobre qué tan poco cuenta accuracy por sí solo.

El problema se vuelve grave, no solo insensible, cuando las clases están desbalanceadas — y el fraude es el ejemplo de manual de desbalance: en un banco real, el fraude puede ser el 0.5% o el 1% de las transacciones, no el 40% del ejemplo de validación de Ignasio.

Supongamos 10,000 transacciones reales, con solo 100 (1%) de fraude. Ignasio entrena un modelo perezoso que aprendió a decir "legítima" siempre, para toda transacción, sin mirar ni un solo feature. Su matriz de confusión: 0 TP, 0 FP, 100 FN, 9,900 TN.

```
accuracy = (0 + 9900) / 10000 = 0.99
```

**99% de accuracy**, y el modelo no detectó ni un solo fraude. Si Ignasio le muestra ese número a su jefe sin contexto, parece un modelo brillante. Pero recall = 0/(0+100) = 0, y precision ni siquiera está definida (0/0, nunca predijo "fraude"). El número que más brilla es justo el que menos dice la verdad.

¿Por qué pasa esto? Porque accuracy cuenta *todos* los aciertos por igual, y cuando una clase es abrumadoramente mayoritaria, basta con acertarle a la clase mayoritaria para inflar el número — sin importar qué tan mal le vaya en la clase que de verdad importa. Los 9,900 TN "ahogan" a los 100 FN en el promedio. Con clases razonablemente balanceadas (40/60, como en el ejemplo de validación de 1.4) este efecto no se nota tanto, porque ninguna clase puede esconderse del todo detrás de la otra; con clases desbalanceadas de verdad, la clase minoritaria — casi siempre la que le interesa detectar a Ignasio — puede desaparecer casi por completo del número final.

La lección práctica: accuracy solo es un resumen confiable cuando las clases están razonablemente balanceadas. En fraude, spam, detección de enfermedades raras, o cualquier problema donde lo que buscás es raro por definición, accuracy es casi un antipatrón — precision, recall y F1, calculados sobre la clase positiva, cuentan una historia mucho más honesta. Y por qué exactamente ese 1% de prevalencia afecta a precision pero no a recall es justo el tema de la siguiente sección.

### El base rate / prevalencia   (por qué precision se mueve con la prevalencia y recall no)

El **base rate** (o **prevalencia**) es simplemente qué fracción de la población real es positiva: `prevalencia = (TP + FN) / total`. En el set de validación de 1.4 era 8/20 = 0.4 (40% fraude); en la Empresa Feliz de verdad, probablemente ronda el 1% o menos. Esa diferencia no es un detalle menor — cambia por completo cuánto se puede confiar en precision, y no le hace nada a recall. Vale la pena ver exactamente por qué.

Mirá de nuevo las fórmulas:

```
recall    = TP / (TP + FN)
precision = TP / (TP + FP)
```

`recall` solo usa números que viven adentro de la clase positiva: TP y FN son, entre los dos, *todo* el fraude real que existe (`TP + FN = prevalencia × total`). No hay ningún término ahí que dependa de cuántas transacciones legítimas hay alrededor. Por eso recall es una propiedad del modelo *sobre la clase fraude en sí* — igual de válida si el fraude es el 40% de las transacciones o el 0.1%.

`precision`, en cambio, tiene FP en el denominador, y los FP salen de la clase negativa — que es enorme cuando el fraude es raro. Ese es el mecanismo: si las legítimas son 9 de cada 10 transacciones (o 99 de cada 100, o 999 de cada 1000), hasta una tasa de falsos positivos chiquita sobre esa masa gigante genera un número absoluto de FP que puede superar por mucho a los TP, que salen de una clase minúscula.

Para verlo con precisión, conviene separar precision en dos ingredientes: recall (qué tan bien atrapa el fraude) y **FPR** (*false positive rate* = `FP / (FP + TN)`, qué tan seguido dispara una falsa alarma sobre una transacción legítima). Con esos dos y la prevalencia π, precision queda así:

```
precision = (recall · π) / (recall · π + FPR · (1 − π))
```

Es la misma cuenta que el teorema de Bayes para "probabilidad de estar enfermo dado un test positivo" — y no es casualidad, es exactamente el mismo problema. `recall` y `FPR` son propiedades del modelo a un umbral dado (no cambian si cambia la población); π es propiedad de *dónde* lo despliegues. La fórmula muestra en blanco y negro que precision mezcla las dos cosas, mientras que recall depende solo de la primera.

Apliquémoslo a Ignasio. En su set de validación de 1.4, a umbral `0.5` tenía recall = 0.75 y FPR = 3/12 = 0.25 (3 FP sobre 12 legítimas). Ahí la prevalencia era 0.4, y su precision fue 0.67. Ahora imaginemos que ese mismo modelo, con ese mismo umbral — ni un score cambia — se despliega en producción, donde el fraude real es apenas 1% de las transacciones (π = 0.01):

```
precision = (0.75 · 0.01) / (0.75 · 0.01 + 0.25 · 0.99)
          = 0.0075 / (0.0075 + 0.2475)
          ≈ 0.029
```

Precision se derrumba de 0.67 a menos de 3%, y recall sigue exactamente en 0.75. Nada del modelo cambió — ni los pesos, ni el umbral, ni siquiera el FPR. Lo único que cambió fue la proporción de fraude en la población donde se mide. En números absolutos: sobre 10,000 transacciones con 100 fraudes reales, ese modelo atraparía 75 fraudes (TP) pero también dispararía 2,475 falsas alarmas (FP) — con una tasa de error sobre legítimas que en el set de validación parecía perfectamente razonable (25%).

Esto conecta directo con lo que vimos en la sección anterior sobre los extremos de la perilla: a `umbral = 0`, donde recall = 1 y FPR = 1 (el modelo marca todo), la fórmula se reduce a `precision = π` — precision colapsa exactamente al base rate. Es el piso absoluto de precision para cualquier modelo, por bueno que sea: ni el mejor modelo del mundo puede tener, en el peor umbral, mejor precision que la prevalencia misma.

La lección práctica para Ignasio: un precision medido en un set de validación con clases más balanceadas que la realidad (algo comunísimo, porque los sets de validación suelen curarse o muestrearse para tener suficientes ejemplos positivos) **no se transfiere a producción**. Reportar "mi modelo tiene 67% de precision" sin decir a qué prevalencia se midió es, en la práctica, casi tan incompleto como no decir a qué umbral. Recall sí viaja razonablemente bien entre poblaciones con distinta prevalencia (siempre que la relación entre el score y la clase real no cambie) — por eso, cuando la clase positiva es rarísima, buena parte de la Parte 3 va a preferir mirar curvas construidas con recall y FPR (ROC) o replantear qué significa "precision" en ese régimen (PR-AUC), en vez de confiar en un precision puntual medido en el dataset equivocado.


## Parte 3 — Métricas que barren TODOS los umbrales (una curva)

### ROC y AUC

La Parte 2 completa vive presa de una limitación: cada métrica se calcula a un umbral fijo. Pero el umbral es una perilla (1.4), así que en vez de congelarla en un valor y reportar un único número, se puede preguntar algo más ambicioso: ¿qué tan bien ordena el modelo los scores, sin comprometerse con ningún umbral en particular? Esa es exactamente la cualidad "ordenar bien" que se separó en 1.2 de "que el número sea creíble". La curva **ROC** (*Receiver Operating Characteristic*) es la primera herramienta para medir eso.

La idea es barrer el umbral desde 1 hasta 0 y, en cada posición, anotar dos números:

```
TPR (recall) = TP / (TP + FN)   — la misma cuenta de 2.2: qué fracción de fraude real atrapa
FPR          = FP / (FP + TN)   — qué fracción de transacciones legítimas dispara una falsa alarma
```

TPR ya se conoce: es el recall de 2.2, con otro nombre (*true positive rate*) porque en la curva ROC conviene mirarlo junto a su contraparte del lado negativo, el FPR. Cada punto (FPR, TPR) resume una matriz de confusión completa en dos coordenadas; recorrer todos los umbrales posibles traza una curva.

Retomemos las 20 transacciones de Ignasio (1.4) y ordenemos las 20 juntas por score, de mayor a menor, acumulando TP y FP a medida que el umbral (imaginario) baja y las va cruzando:

| score | real | TP acum. | FP acum. | TPR (recall) | FPR |
|---|---|---|---|---|---|
| 0.93 | Fraude | 1 | 0 | 0.125 | 0 |
| 0.85 | Fraude | 2 | 0 | 0.25 | 0 |
| 0.79 | Fraude | 3 | 0 | 0.375 | 0 |
| 0.70 | Fraude | 4 | 0 | 0.5 | 0 |
| 0.66 | Legítima | 4 | 1 | 0.5 | 0.083 |
| 0.62 | Fraude | 5 | 1 | 0.625 | 0.083 |
| 0.58 | Legítima | 5 | 2 | 0.625 | 0.167 |
| 0.54 | Fraude | 6 | 2 | 0.75 | 0.167 |
| 0.50 | Legítima | 6 | 3 | 0.75 | 0.25 |
| 0.47 | Fraude | 7 | 3 | 0.875 | 0.25 |
| 0.43 | Legítima | 7 | 4 | 0.875 | 0.333 |
| 0.37 | Legítima | 7 | 5 | 0.875 | 0.417 |
| 0.36 | Fraude | 8 | 5 | 1.0 | 0.417 |

De ahí en más no queda fraude por atrapar: las siete legítimas restantes (`0.31` a `0.02`) solo van empujando el FPR de 0.417 hasta 1.0 sin mover más el recall, hasta llegar a `umbral = 0` (todo marcado "fraude") en el punto (1, 1).

Fijate en tres filas marcadas: la de score `0.50` (umbral 0.5 de 1.4: TP=6, FP=3 → recall=0.75, FPR=0.25), la de score `0.66` (umbral 0.65: TP=4, FP=1 → recall=0.5, FPR=0.083) y la de score `0.36` (umbral 0.35: TP=8, FP=5 → recall=1.0, FPR=0.417). Son exactamente los tres umbrales que se recorrieron en 1.4 — ahora son tres puntos sobre la misma curva, no tres experimentos sueltos.

Uniendo todos los puntos —empezando en (0,0), umbral=1, nada cruza— y terminando en (1,1) —umbral=0, todo cruza— se obtiene la curva ROC completa del modelo. Un modelo que ordenara perfecto (todos los fraudes con score más alto que todas las legítimas) treparía pegado al eje vertical hasta (0,1) y después iría recto a (1,1): atrapa el 100% del fraude sin ni una falsa alarma. Un modelo que solo adivina al azar traza la diagonal (0,0)→(1,1): cualquier FPR que se acepte da ese mismo TPR, sin ninguna ganancia por ordenar.

**AUC** (*area under the curve*) resume la curva entera en un solo número: el área bajo ella, entre 0 y 1. Integrando los trapecios de la tabla de arriba, el modelo de Ignasio da AUC ≈ 0.885.

Hay una lectura más intuitiva de ese 0.885, que conecta directo con "ordenar bien" (1.2): AUC es la probabilidad de que, tomando una transacción fraudulenta al azar y una legítima al azar, el modelo le dé mayor score a la fraudulenta. Es literalmente lo que hay detrás de la tabla: de los 8×12 = 96 pares posibles (una fraude, una legítima), en 85 de ellos el fraude queda por encima — 85/96 ≈ 0.885. Un AUC de 0.5 es un modelo que ordena como una moneda al aire; un AUC de 1.0 es separación perfecta; 0.885 dice que Ignasio va bastante bien, muy por encima del azar, aunque lejos de perfecto — coherente con que las dos distribuciones de scores se solapaban, como ya se vio en 1.4.

Importante: AUC no depende de ningún umbral — es la misma con el umbral en 0.5, en 0.35 o en 0.9999, porque resume la curva entera, no un punto de ella. Eso la hace ideal para comparar dos modelos ("¿cuál ordena mejor, en general?") sin tener que acordar primero dónde va la perilla — esa discusión queda para después, una vez elegido el mejor candidato.

### La curva Precision–Recall y Average Precision (PR-AUC)

La curva ROC usa FPR, y FPR tiene TN en el denominador — la clase legítima, que en la Empresa Feliz real es gigantesca (fraude ≈1%, sección 2.5). La curva **Precision-Recall (PR)** cambia el eje: en vez de (FPR, TPR), grafica (recall, precision) — la misma perilla barrida, pero mirando la pregunta que de verdad le importa al equipo que revisa alarmas: de las que el modelo marca, ¿cuántas son reales?

Reutilizando la misma tabla ordenada de arriba, ahora con precision en vez de FPR (precision solo está definida donde hay al menos un TP o FP, es decir, donde el modelo ya predijo "fraude" alguna vez), y mostrando solo los puntos donde entra un TP nuevo — que es donde el recall se mueve:

| umbral (score) | TP acum. | FP acum. | recall | precision |
|---|---|---|---|---|
| 0.93 | 1 | 0 | 0.125 | 1.0 |
| 0.85 | 2 | 0 | 0.25 | 1.0 |
| 0.79 | 3 | 0 | 0.375 | 1.0 |
| 0.70 | 4 | 0 | 0.5 | 1.0 |
| 0.62 | 5 | 1 | 0.625 | 0.833 |
| 0.54 | 6 | 2 | 0.75 | 0.75 |
| 0.47 | 7 | 3 | 0.875 | 0.7 |
| 0.36 | 8 | 5 | 1.0 | 0.615 |

(Entre esos puntos hay pasos intermedios donde solo entra un FP: ahí el recall no se mueve, pero la precision cae un poco más — por ejemplo entre `0.66` y `0.62` o entre `0.58` y `0.54` en la tabla de la sección anterior. Lo esencial de la forma de la curva ya se ve en los saltos de recall.)

La forma típica de esta curva es "empezar arriba a la izquierda y caer hacia la derecha": con pocos casos marcados (umbral alto), casi todo lo que el modelo señala es fraude de verdad (precision alta), pero el recall es bajo. A medida que se baja el umbral para atrapar más fraude, cada fraude nuevo que se suma viene acompañado de más legítimas que también cruzan la línea, y la precision va cediendo terreno — es la misma tensión precision-recall de la sección 2.3, ahora dibujada en vez de descrita.

**Average Precision (AP)**, el equivalente del AUC para esta curva, se calcula promediando la precision en cada punto donde aparece un TP nuevo, ponderada por cuánto subió el recall en ese paso:

```
AP = Σ (recall_n − recall_(n−1)) · precision_n
```

Con los 8 saltos de recall del modelo de Ignasio (cada uno de tamaño 1/8 = 0.125, porque cada fraude real suma lo mismo al recall):

```
AP = 0.125 · (1.0 + 1.0 + 1.0 + 1.0 + 0.833 + 0.75 + 0.7 + 0.615) ≈ 0.862
```

AP ≈ 0.862 — parecido al AUC (0.885) en este ejemplo, y no es casualidad: ambos resumen la misma familia de curvas. Donde sí difieren de fondo es en su punto de referencia. La diagonal de ROC (el azar) siempre vale 0.5, sin importar la prevalencia. El modelo tramposo de las secciones 2.2 y 2.4 — el que no distingue nada entre clases — en la curva PR traza en cambio una línea horizontal en `precision = prevalencia` (0.4 en este set de validación), no en 0.5. Dicho de otro modo: el nivel de "no hace nada mejor que el azar" en PR-AUC depende de qué tan común es el fraude en los datos, cosa que ROC-AUC no hereda. Eso importa mucho para la pregunta de la siguiente sección.

### ROC vs PR   (cuál usar cuando la clase positiva es rarísima — tu caso)

Ya se vio en 2.5 el mecanismo exacto: recall y FPR son propiedades del modelo que no cambian cuando cambia la prevalencia de la población donde se despliega, pero precision sí, porque mezcla el recall con la prevalencia y el FPR. Ese mismo mecanismo dice de inmediato qué le pasa a cada curva cuando Ignasio despliega su modelo en producción, donde el fraude real es ≈1% y no el 40% artificialmente balanceado de su set de validación.

La curva ROC está construida enteramente con TPR y FPR — ningún ingrediente de la fórmula de 2.5 depende de π. Así que la curva ROC (y su AUC ≈ 0.885) es *exactamente la misma*, tanto en el set de validación balanceado como en producción con 1% de fraude. Suena tranquilizador, pero es justo la trampa: la curva ROC no se entera de que el problema cambió.

La curva PR sí se entera, porque precision depende de π. Aplicando la fórmula de 2.5 (`precision = recall·π / (recall·π + FPR·(1−π))`) con π = 0.01 en vez de 0.4, a los mismos pares (recall, FPR) de la tabla ROC:

| recall | FPR | precision (π=0.4, validación) | precision (π=0.01, producción) |
|---|---|---|---|
| 0.125 – 0.5 | 0 | 1.0 | 1.0 |
| 0.625 | 0.083 | 0.833 | ≈0.070 |
| 0.75 | 0.167 | 0.75 | ≈0.044 |
| 0.875 | 0.25 | 0.7 | ≈0.034 |
| 1.0 | 0.417 | 0.615 | ≈0.024 |

Con esos números, el AP en producción cae de 0.862 a ≈0.52 — el mismo modelo, ni un score cambiado, y la curva PR se derrumba porque ahora cada FPR chiquito genera un número absoluto enorme de falsas alarmas comparado con los pocos fraudes reales que hay para atrapar. El AUC-ROC, mientras tanto, sigue clavado en 0.885 — un espejismo de estabilidad.

Esa es la respuesta a "cuál usar": cuando la clase positiva es rarísima —fraude, spam, enfermedades raras— **la curva PR (y AP) es la que hay que mirar**, porque refleja lo que de verdad va a vivir el equipo que revisa alarmas o el cliente al que le bloquean la tarjeta: cuántas de las alarmas son reales. ROC-AUC no está "mal", pero puede quedarse alta y estable mientras la precision se derrumba en silencio, dándole a Ignasio una falsa sensación de que nada cambió al pasar de validación a producción.

La regla práctica: usar ROC/AUC para comparar el poder de ranking puro de dos modelos, sobre todo si las clases están razonablemente balanceadas o si el costo de FP y FN es simétrico. Usar PR/AP cuando la clase positiva es minoritaria y lo que importa es la experiencia real del sistema en producción — que es, sin rodeos, el caso de la Empresa Feliz.

## Parte 4 — ¿Ordena bien, o además le atina a la probabilidad?

### Discriminación vs calibración   (AUC mide ranking, no probabilidades creíbles)

En 1.2 se separaron dos cualidades del score que son independientes entre sí: **ordenar bien** (darle score más alto a los fraudes reales que a las legítimas) y **que el número sea una probabilidad creíble** (si dice `0.8`, que de verdad ronde el 80% de los casos parecidos sean fraude). Toda la Parte 3 —ROC, AUC, PR, AP— midió exclusivamente la primera cualidad. A esa primera cualidad se la llama **discriminación**; a la segunda, **calibración**. Vale la pena demostrar, con números, que son de verdad independientes — no es solo una advertencia teórica.

**Discriminación sin calibración.** Tomemos el modelo de Ignasio (llamémoslo M1, el de 1.4) y construyamos un segundo modelo M2 aplicándole a cada score una transformación de "temperatura" que lo hace más extremo, más cerca de 0 o de 1:

```
logit(p) = ln(p / (1 − p))
M2(p) = sigmoide(3 · logit(p))
```

Es una transformación estrictamente monótona (si `p_a > p_b`, entonces `M2(p_a) > M2(p_b)`, siempre), así que **no cambia ni un solo orden relativo** entre los 20 scores de Ignasio. Por eso AUC(M2) = AUC(M1) ≈ 0.885 — la curva ROC es idéntica, porque AUC solo cuenta, para cada par (una fraude, una legítima), quién queda arriba, y eso no se altera. Pero mirá lo que le pasa a los valores concretos:

| transacción | score M1 | score M2 (temperatura ×3) |
|---|---|---|
| 0.36 (fraude real) | 0.36 | ≈ 0.15 |
| 0.62 (fraude real) | 0.62 | ≈ 0.81 |
| 0.66 (legítima real) | 0.66 | ≈ 0.88 |

M2 ordena exactamente igual que M1 (0.15 < 0.81 < 0.88, el mismo orden que 0.36 < 0.62 < 0.66), pero como número, es una mentira: le dice a un fraude real de verdad ("0.36") que su probabilidad de ser fraude bajó a 15%, y le dice a una transacción legítima ("0.66") que es 88% probable que sea fraude. Cualquiera que tome esos números al pie de la letra —para calcular una pérdida esperada, por ejemplo— se lleva una sorpresa desagradable. Mismo poder de ranking, calibración muchísimo peor.

**Calibración sin discriminación.** El caso simétrico también existe. Imaginemos un modelo M3 tramposo que ignora los datos de entrada y le asigna a *toda* transacción el mismo score: la prevalencia observada, `0.4` (la de 1.4). En promedio, M3 está perfectamente calibrado — el 40% de las veces que "dice" 0.4, en efecto es fraude, porque el 40% de todas las transacciones lo son. Pero M3 no distingue nada entre una transacción y otra: todos los scores son idénticos, así que no hay ningún par (fraude, legítima) donde uno quede por encima del otro — están todos empatados. Por convención, un empate cuenta como medio acierto, y con el 100% de los pares empatados, AUC(M3) = 0.5: rendimiento de moneda al aire. Calibración perfecta, discriminación nula.

Moraleja: ni AUC ni PR-AUC dicen nada sobre si el número en sí es creíble, y una calibración perfecta en el agregado tampoco garantiza que el modelo distinga nada. Hacen falta ambas cosas, y hace falta una herramienta separada para medir la segunda — la de la siguiente sección.

### Calibración   (reliability diagram, Brier, ECE — cuándo importa)

Si discriminación es "¿el orden es correcto?", calibración es una pregunta distinta: **de todas las veces que el modelo dijo *aproximadamente p*, ¿qué fracción resultó ser fraude de verdad?** Un modelo calibrado, cuando dice `0.8`, acierta cerca del 80% de esas veces — ni más, ni menos.

**El reliability diagram** es la forma más directa de verlo: se agrupan los ejemplos en baldes según su score y, para cada balde, se compara el score promedio (lo que el modelo "cree") contra la fracción real de fraude en ese balde (lo que en verdad pasó). Sobre las 20 transacciones de Ignasio, usando baldes de ancho 0.25:

| balde de score | n | score promedio (confianza) | fracción real de fraude (observado) |
|---|---|---|---|
| [0.75, 1.0] | 3 | 0.857 | 1.0 |
| [0.50, 0.75) | 6 | 0.600 | 0.5 |
| [0.25, 0.50) | 6 | 0.367 | 0.333 |
| [0, 0.25) | 5 | 0.106 | 0.0 |

Si el modelo estuviera perfectamente calibrado, cada fila tendría confianza = observado, y los cuatro puntos caerían sobre la diagonal en un gráfico (confianza en x, observado en y). Acá andan cerca pero no exactos: en el balde alto el modelo es levemente *sub*confiado (dice 0.857, la realidad fue 1.0 — pudo haber sido más seguro), y en el balde medio es levemente *sobre*confiado (dice 0.6, la realidad fue 0.5). Nada dramático — es el mismo tipo de desvío que separaba a M1 de M2 en la sección anterior, pero mucho más leve.

**ECE** (*Expected Calibration Error*) resume el reliability diagram completo en un solo número: el promedio de esas diferencias, ponderado por cuántos ejemplos cayeron en cada balde.

```
ECE = Σ (n_balde / n_total) · |confianza_balde − observado_balde|
```

Con la tabla de arriba: `ECE = 0.15·|0.857−1.0| + 0.30·|0.6−0.5| + 0.30·|0.367−0.333| + 0.25·|0.106−0| ≈ 0.15·0.143 + 0.30·0.1 + 0.30·0.034 + 0.25·0.106 ≈ 0.088`. Un ECE de 0 sería calibración perfecta; 0.088 es un desvío chico — nada parecido a lo que le pasaría a M2 de la sección anterior, cuyos baldes extremos quedarían muy lejos de la diagonal.

**Brier score** es otra forma de medir lo mismo, sin necesidad de agrupar en baldes: el error cuadrático medio entre el score y la etiqueta real (1 si fue fraude, 0 si no).

```
Brier = (1/n) · Σ (score_i − y_i)²
```

Para el modelo de Ignasio sobre las 20 transacciones, Brier ≈ 0.14. Para darle contexto a ese número: el modelo tramposo M3 de la sección anterior (siempre predice `0.4`, perfectamente calibrado en el agregado pero sin discriminación) tiene Brier = 0.4²·0.6 + 0.6²·0.4 = 0.24 — peor que el de Ignasio, a pesar de estar "bien calibrado". Eso es porque Brier, a diferencia de ECE, no mide *solo* calibración: mezcla discriminación y calibración en un único número (por eso M3, con discriminación nula, sale peor que M1 pese a estar mejor calibrado en el agregado). Es útil como resumen general, pero si lo que se quiere aislar es específicamente "¿el número es creíble?", el reliability diagram y el ECE son las herramientas más limpias, porque separan esa pregunta de la pregunta del ranking.

**¿Cuándo le importa esto a Ignasio?** Depende de qué se hace con el score después de calcularlo:

- Si el score solo se usa para **ordenar** transacciones y revisar las top-K más sospechosas, o para **umbralizar una vez** y nunca más mirar el número crudo, la calibración casi no importa — lo único que cuenta es la discriminación (AUC / PR-AUC de la Parte 3), y hasta un modelo tan mal calibrado como M2 serviría igual de bien.
- Si el score se usa para calcular una **pérdida esperada** — por ejemplo, priorizar la cola de revisión multiplicando `P(fraude) × monto de la transacción`, para atender primero los casos de mayor riesgo en dólares — la calibración es central: dos transacciones con el mismo monto pero scores de 0.3 y 0.9 deben reflejar de verdad una diferencia real de 3× en probabilidad, no un artefacto de cómo quedó entrenado el modelo.
- Si el score de este modelo se va a **combinar con otros** (otro modelo, una regla de negocio, un score de otro sistema) mediante promedios o actualización bayesiana, todos los números tienen que significar lo mismo — combinar un score bien calibrado con uno mal calibrado da un resultado sin sentido.
- Si el score se **le muestra directamente a una persona** ("87% de probabilidad de fraude") que va a confiar en ese número tal cual, un modelo mal calibrado la engaña sistemáticamente, aunque ordene perfecto.
- Y, mirando hacia adelante: elegir el umbral óptimo con una matriz de costos (Parte 6) generalmente asume que el score aproxima una probabilidad real — un modelo con gran discriminación pero mal calibrado puede llevar a elegir el umbral equivocado, aunque su AUC luzca excelente.

Cuando la calibración falla pero la discriminación es buena (el caso de M2), no hace falta reentrenar el modelo: alcanza con un ajuste posterior *monótono* —como Platt scaling (ajustar una regresión logística sobre los scores) o isotonic regression— que recalibra los números sin tocar el orden, y por lo tanto sin tocar el AUC. Es, literalmente, deshacer la transformación de temperatura que se usó para construir M2.