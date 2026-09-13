# Diagnóstico y mediciones para algoritmos de ML de clasificación

Supongamos un investigador/ingeniero ML llamado Ignasio en una empresa ficticia llamada la "Empresa Feliz". Ignasio tiene la tarea de entrenar un modelo que clasifique correctamente transacciones como fraudulentas o legítimas.

Para ello se le suministran permisos de acceso en base de datos para consultar transacciones historicas. Ignasio está feliz porque usó pytorch para crear su MLP con el módulo `n.n`, sin embargo después de un entrenamiento de varios días con su pc encendido consumiendo electricidad con su RTX 5070 viene una pregunta muy importante y fundamental: **¿Esto si está aprendiendo a clasificar?**

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

El modelo no dice "esto es fraude": ajusta una recta y la aplana con la sigmoide para dar un número entre 0 y 1 (un **score**), interpretado como "qué tan probable es fraude". La decisión ("fraude" / "no fraude") es un paso aparte: comparar ese score contra un umbral, típicamente `0.5`.

Si evaluamos solo la decisión final perdemos información: un score `0.51` y uno `0.9` caen del mismo lado del umbral, pero el segundo lo dice con mucha más **confianza**. Esa diferencia es justo lo que delata si el modelo entendió el problema o está **adivinando** cerca del borde.

Por eso conviene evaluar el score en sí antes de hablar de umbrales. Tiene dos cualidades independientes entre sí:

- **Ordenar bien**: ¿les da score más alto a los fraudes de verdad que a las legítimas? No importa el valor exacto, importa el orden relativo. Un modelo que da `0.05` a fraudes y `0.02` a legítimas ordena perfecto aunque ningún score "parezca" alto.
- **Que el número sea una probabilidad creíble**: si dice `0.8`, ¿de verdad ronda el 80% de fraude entre todos los casos donde dijo algo cercano a `0.8`? Se puede ordenar perfecto y estar mal calibrado — por ejemplo diciendo `0.95` cuando la tasa real ronda el 60%.

#### Ejemplo 1 — Ordenar bien

Seis transacciones, dos modelos con scores distintos:

| transacción | real     | Modelo A | Modelo B |
|-------------|----------|----------|----------|
| t1          | Fraude   | 0.90     | 0.09     |
| t2          | Fraude   | 0.85     | 0.085    |
| t3          | Fraude   | 0.70     | 0.07     |
| t4          | Legítima | 0.30     | 0.03     |
| t5          | Legítima | 0.20     | 0.02     |
| t6          | Legítima | 0.10     | 0.01     |

Los dos **ordenan idéntico** (mismo AUC = 1.0, separación perfecta), aunque el Modelo B nunca dice un número que "parezca" fraude (máximo `0.09`).

> **La idea:** ordenar bien no depende de la magnitud, depende de quién queda arriba de quién. Un fraude con `0.09` y una legítima con `0.01` está perfectamente ordenado, aunque ningún número supere el `0.5`.

Esto es lo que miden **ROC / AUC** y **PR / AP**.

#### Ejemplo 2 — Que el número sea una probabilidad creíble (calibración)

El modelo "dice 80%" en el instante en que asigna `0.8`. Verificar si es honesto es un paso posterior: juntar todos los casos donde dijo `0.8` y ver qué pasó de verdad.

##### Un solo nivel (el 0.8)

De 10 transacciones donde el modelo dijo ~`0.8`:

- **Calibrado:** 8 resultaron fraude. El 80% real fue fraude — el número es creíble.
- **Mal calibrado (sobreconfiado):** solo 6 resultaron fraude. Dice `0.8` pero la tasa real ronda 60% — el número miente.

##### Todos los niveles a la vez (reliability diagram)

Igual pero en **rangos (baldes)**, porque los scores son continuos:

| balde de score | modelo dice (promedio) | pasó de verdad |
|----------------|------------------------|-----------------|
| [0.0, 0.2)     | ~0.10                  | ¿qué fracción fue fraude? |
| [0.2, 0.4)     | ~0.30                  | ¿qué fracción fue fraude? |
| [0.4, 0.6)     | ~0.50                  | ¿qué fracción fue fraude? |
| [0.6, 0.8)     | ~0.70                  | ¿qué fracción fue fraude? |
| [0.8, 1.0]     | ~0.90                  | ¿qué fracción fue fraude? |

Un modelo bien calibrado tiene, en **cada** balde, "lo que dice" ≈ "lo que pasó".

> **Analogía:** un pronosticador que dice "80% de lluvia" ya lo dijo en ese momento; que sea bueno se sabe después, viendo si llovió en 8 de cada 10 días que dijo "80%". El modelo es el pronosticador; el score es el "80%"; la calibración es revisar su historial.

Esto es lo que miden **reliability diagram**, **ECE** y **Brier score**.

##### Lo clave: son independientes

- **Modelo B** (ejemplo 1) ordena impecable pero sus números (`0.09`, `0.01`) son ridículamente bajos → buena discriminación, mala calibración.
- Un modelo **sobreconfiado** puede ordenar perfecto e inflar los números (`0.8` cuando es 60%) → buena discriminación, mala calibración.
- Un modelo que asigna a **todo** la prevalencia (ej. `0.4`) está calibrado en agregado pero no distingue nada → mala discriminación, buena calibración.

Se miden con herramientas distintas porque son independientes: puede ordenar de maravilla con números sistemáticamente desviados, o tener números creíbles con orden mediocre. **ROC/AUC y PR/AP** miden el orden (Parte 3); **reliability diagram, ECE y Brier** miden la credibilidad del número (Parte 4).


### 1.3 La matriz de confusión: TP, FP, FN, TN

Convertida la decisión (score vs. umbral), se cruza contra la verdad y salen cuatro casos:

| | Real: Fraude | Real: Legítima |
|---|---|---|
| **Predicho: Fraude** | True Positive (TP) | False Positive (FP) |
| **Predicho: Legítima** | False Negative (FN) | True Negative (TN) |

- **TP**: era fraude, dijo fraude — atrapado.
- **TN**: era legítima, dijo legítima — cliente honesto tranquilo.
- **FP**: era legítima, dijo fraude — falsa alarma, tarjeta bloqueada sin razón.
- **FN**: era fraude, dijo legítima — el peor caso, el fraude pasa como si nada.

Esta matriz es la materia prima de precision, recall, F1 y accuracy (Parte 2) — distintas formas de combinar estos cuatro números. Pero depende de un umbral fijo: al moverlo, TP se vuelven FN, TN se vuelven FP, y la matriz cambia entera.

### 1.4 El umbral de decisión

El `0.5` es solo la convención por defecto — el umbral es puro post-proceso, tan fácil de cambiar como una línea de código, y moverlo cambia la matriz entera.

Ignasio corre el modelo sobre 20 transacciones de validación. Ocho eran fraude de verdad, con scores:

`0.93, 0.85, 0.79, 0.70, 0.62, 0.54, 0.47, 0.36`

Doce eran legítimas de verdad:

`0.66, 0.58, 0.50, 0.43, 0.37, 0.31, 0.26, 0.20, 0.15, 0.10, 0.06, 0.02`

Los grupos se solapan (hay legítimas con score `0.66`, más alto que un fraude con `0.36`) — lo normal en un modelo real, y justo lo que hace importar la posición del umbral.

- **Umbral `0.5`**: cruzan seis fraudes (TP) y dos quedan afuera (FN); de las legítimas cruzan tres (FP) y nueve quedan afuera (TN) → **6 TP, 3 FP, 2 FN, 9 TN**.
- **Umbral `0.35`**: los ocho fraudes cruzan (0 FN), pero también cinco legítimas más → **8 TP, 5 FP, 0 FN, 7 TN** — todo el fraude atrapado, a costa de más falsas alarmas.
- **Umbral `0.65`**: cuatro fraudes dejan de cruzar (FN); solo una legítima sigue como FP → **4 TP, 1 FP, 4 FN, 11 TN** — casi sin falsas alarmas, pero se escapa la mitad del fraude real.

Ningún score cambió entre los tres escenarios — solo la perilla del umbral, y eso bastó para reacomodar toda la matriz. Por eso no tiene sentido decir "mi modelo tiene 90% de precision" sin aclarar a qué umbral.

> Simulador interactivo: [html/score_umbral_metricas_prevalencia.html](html/score_umbral_metricas_prevalencia.html). Cubre desde el riesgo empírico vs verdadero (1.1) hasta la prevalencia (2.5): un slider mueve el umbral sobre las mismas 20 transacciones y recalcula en vivo la matriz de confusión, precision, recall, accuracy y FPR; otro slider mueve la prevalencia y muestra cómo se derrumba precision al pasar de validación a producción.

¿Quién decide dónde poner la perilla? El negocio. Bajar el umbral favorece recall (más fraude atrapado) a costa de más clientes honestos molestos; subirlo favorece precision (menos falsas alarmas) a costa de más fraude escapado. Cuál error sale más caro es el tema de la Parte 6 (matriz de costos). Por ahora: el umbral es una decisión aparte del modelo, no una propiedad suya.

## Parte 2 — Métricas a UN umbral fijo (un punto)

### 2.1 Precision

Con umbral `0.5` (6 TP, 3 FP, 2 FN, 9 TN):

> De todas las veces que el modelo gritó "¡fraude!", ¿cuántas veces tenía razón?

```
precision = TP / (TP + FP)
```

El modelo marcó "fraude" nueve veces y acertó en seis: precision = 6/9 ≈ 0.67 — dos de cada tres alarmas son reales, la tercera es un cliente honesto bloqueado sin motivo.

Por qué le importa a la Empresa Feliz: cada FP es un cliente real rechazado, enojado, que quizás se cambia de banco. Precision baja entierra en falsas alarmas al equipo que revisa casos y erosiona la credibilidad del modelo.

Caso extremo: un modelo tramposo que casi nunca dice "fraude" —solo cuando está segurísimo— puede lograr precision 1.0 sin atrapar casi nada. Precision alta no significa "atrapa mucho fraude", significa "cuando actúa, no se equivoca". Eso lo mide recall.

### 2.2 Recall

Si precision mira la fila "Predicho: Fraude", **recall** mira la columna "Real: Fraude":

> De todos los fraudes que de verdad ocurrieron, ¿cuántos atrapó el modelo?

```
recall = TP / (TP + FN)
```

Con umbral `0.5` (6 TP, 2 FN): recall = 6/8 = 0.75 — atrapó tres de cada cuatro; se le escaparon los dos fraudes de score más bajo (`0.47`, `0.36`). Precision en ese mismo punto era 0.67 — parecido pero no igual, ambas miden cosas distintas.

Con umbral `0.65` (4 TP, 4 FN): recall = 4/8 = 0.5. Subir la perilla ganó precision (0.67→0.8) pero costó la mitad del recall.

> Recall no le importan las falsas alarmas, solo no dejar pasar fraude real. Por eso también se llama **sensitivity** o **true positive rate** — reaparece en la curva ROC (Parte 3).

Por qué le importa a la Empresa Feliz: cada FN es plata perdida y un cliente que puede culpar al banco por no detectar el robo. Si un fraude no detectado cuesta más que molestar a un cliente honesto, conviene recall alto aunque cueste precision — la pregunta del umbral correcto se retoma en la Parte 6.

Caso extremo simétrico: marcar *todo* como fraude da recall 1.0 perfecto (nada se le escapa porque nada pasa), con precision pésima. Ningún extremo sirve solo — de esa tensión trata la siguiente sección.

### La tensión precision–recall (por qué no podés maximizar las dos)

Al mover el umbral de 0.5 a 0.65, Ignasio ganó precision (0.67→0.8) y perdió recall (0.75→0.5). No es mala suerte puntual: es estructural.

En `umbral = 0` (todo marcado fraude): recall = 8/8 = 1.0, precision = 8/20 = 0.4 (exactamente el base rate). En `umbral = 1` (nada marcado): precision indefinida (0/0), recall = 0.

Entre extremos, cada caso que deja de cruzar la línea al subir el umbral era, antes, TP o FP. Si era FP, precision sube; si era TP se vuelve FN y recall baja. En la práctica ambas cosas se mueven a la vez, en direcciones opuestas.

Es geométrico, no una limitación de Ignasio: TP y FP viven del mismo lado de la línea ("predicho fraude"), así que cualquier movimiento los afecta juntos. No hay umbral mágico que maximice ambas a la vez, salvo un clasificador perfecto sin solapamiento.

Por eso "mi modelo tiene 95% de precision/recall" es incompleto sin decir a qué umbral, y comparar modelos con una sola métrica es tramposo — alguien pudo mover la perilla. Hace falta resumir el compromiso en un número (F1) o comparar sin comprometerse a un umbral (curva PR, Parte 3).

### F1 (y por qué media armónica y no promedio normal)

La tentación es promediar: `(precision + recall) / 2`. Es una trampa.

Modelo tramposo que marca *todo* como fraude: recall = 1.0, pero si el 1% es fraude, precision ronda 0.01. Media aritmética: `(0.01 + 1.0)/2 = 0.505` — suena "aceptable" y es falso: el modelo bloquea a todo el mundo.

La media aritmética deja que un número alto tape a uno bajo. Hace falta una media que castigue fuerte cuando cualquiera de los dos es malo: la **media armónica**, que define **F1**:

```
F1 = 2 · (precision · recall) / (precision + recall)
```

Con el modelo tramposo: `F1 = 2·(0.01·1.0)/(0.01+1.0) ≈ 0.0198` — ahí sí queda claro que es malo, porque la media armónica es dominada por el término más chico. Cuando precision y recall son parecidos, F1 se acerca a la media aritmética; la diferencia solo importa cuando uno está cojo.

Con los números reales de Ignasio a umbral `0.5` (precision ≈ 0.67, recall = 0.75): `F1 ≈ 0.706` — honesto, ni tan optimista como recall solo ni tan pesimista como precision sola.

Dos advertencias:

- F1 sigue siendo a **umbral fijo** — hereda el problema de 1.4. Cambiar el umbral cambia F1.
- F1 pesa igual precision y recall, como si a la Empresa Feliz le doliera igual un FP que un FN. Casi nunca es así (Parte 6) — para eso existe **F-beta**, que pondera uno más que el otro. F1 es el caso balanceado de esa familia.

### Accuracy y por qué miente con clases desbalanceadas

La métrica más obvia:

> ¿qué fracción de todas las predicciones fueron correctas?

```
accuracy = (TP + TN) / (TP + FP + FN + TN)
```

Con umbral `0.5` (6 TP, 3 FP, 2 FN, 9 TN): accuracy = 15/20 = 0.75. Pero a `0.35` y a `0.65` también da 15/20 = 0.75 — tres umbrales con precision moviéndose de 0.62 a 0.8 y recall de 1.0 a 0.5, y accuracy clavada en el mismo número las tres veces. Ya es una señal de alerta.

El problema se vuelve grave con clases desbalanceadas — el fraude es el ejemplo de manual: en un banco real puede ser 0.5%–1%, no el 40% del set de validación de Ignasio.

Con 10,000 transacciones y 100 (1%) de fraude, un modelo perezoso que siempre dice "legítima" da: 0 TP, 0 FP, 100 FN, 9,900 TN →

```
accuracy = 9900 / 10000 = 0.99
```

**99% de accuracy** sin detectar ni un fraude. recall = 0, precision indefinida (0/0). El número que más brilla es el que menos dice la verdad.

Accuracy cuenta todos los aciertos por igual: cuando una clase domina, basta acertarle a ella para inflar el número sin importar la clase que de verdad importa. Con clases balanceadas (40/60) el efecto se nota menos; con desbalance real, la clase minoritaria —la que le interesa a Ignasio— puede desaparecer del número final.

Lección: accuracy solo es confiable con clases razonablemente balanceadas. En fraude, spam, enfermedades raras, es casi un antipatrón — precision, recall y F1 sobre la clase positiva cuentan una historia más honesta.

### FPR (false positive rate) — el espejo de recall

Recall mira la columna "Real: Fraude". Existe la pregunta simétrica sobre la otra columna:

> De los clientes honestos reales, ¿a cuántos les disparé una falsa alarma?

```
FPR = FP / (FP + TN)
```

Con la matriz a umbral `0.5` (3 FP, 9 TN): FPR = 3/12 = 0.25 — uno de cada cuatro clientes honestos recibe una alarma inmerecida.

FPR es una métrica de pleno derecho, tan legítima como recall — no un subproducto. Su complemento, `1 − FPR = TN/(FP+TN)`, se llama **specificity** (o *true negative rate*), usada en medicina junto a *sensitivity* (recall con otro nombre).

FPR reaparece en dos roles: junto con recall explica la dependencia de precision con la prevalencia (próxima sección), y es el eje horizontal de la curva ROC (Parte 3).

### El base rate / prevalencia (por qué precision se mueve con la prevalencia y recall no)

El **base rate** (o **prevalencia**, **π**)

> es la fracción de la población real que es positiva: `π = (TP + FN) / total`.

En el set de validación era π = 8/20 = 0.4; en producción real probablemente ronda 1% o menos. Esa diferencia cambia por completo cuánto se puede confiar en precision, y no le hace nada a recall.

```
recall    = TP / (TP + FN)
precision = TP / (TP + FP)
```

`recall` solo usa TP y FN, que juntos son *todo* el fraude real (`TP+FN = π·total`) — no depende de cuántas legítimas hay alrededor. Es una propiedad del modelo sobre la clase fraude en sí.

`precision` tiene FP en el denominador, y los FP salen de la clase negativa — enorme cuando el fraude es raro. Aunque el FPR sea chico, sobre una masa gigante de legítimas genera un número absoluto de FP que puede superar a los TP.

Reescribiendo la misma fórmula de precision con `TP = recall·π·total` y `FP = FPR·(1−π)·total` (el `total` se cancela):

```
precision = (recall · π) / (recall · π + FPR · (1 − π))
```

Mismo número de siempre — solo cambian las variables: recall y FPR (propiedades del modelo a un umbral dado, no cambian con la población) y π (propiedad de *dónde* se despliega). Es la misma cuenta que el teorema de Bayes para "probabilidad de estar enfermo dado un test positivo".

Aplicado a Ignasio: en validación (π=0.4, recall=0.75, FPR=0.25) precision fue 0.67. En producción (π=0.01), mismo modelo, mismo umbral:

```
precision = (0.75·0.01) / (0.75·0.01 + 0.25·0.99) ≈ 0.029
```

Precision se derrumba de 0.67 a menos de 3%, recall sigue en 0.75 — nada del modelo cambió, solo la proporción de fraude en la población. En absolutos: sobre 10,000 transacciones con 100 fraudes, el modelo atraparía 75 (TP) pero dispararía 2,475 falsas alarmas (FP).

En `umbral = 0` (recall=1, FPR=1) la fórmula se reduce a `precision = π` — el piso absoluto de precision para cualquier modelo, por bueno que sea.

Lección práctica: un precision medido en un set con clases más balanceadas que la realidad **no se transfiere a producción**. "Mi modelo tiene 67% de precision" sin decir a qué prevalencia es casi tan incompleto como no decir a qué umbral. Recall sí viaja bien entre poblaciones distintas — por eso, con clase positiva rarísima, conviene mirar curvas construidas con recall y FPR (ROC) o replantear precision en ese régimen (PR-AUC), en vez de un precision puntual del dataset equivocado.


## Parte 3 — Métricas que barren TODOS los umbrales (una curva)

> Simulador interactivo: [html/roc_pr_calibracion.html](html/roc_pr_calibracion.html). Continúa el simulador de la Parte 1-2 con el mismo ejemplo de 20 transacciones: un umbral compartido recorre a la vez la curva ROC y la curva PR (Parte 3), un slider de prevalencia muestra por qué la curva PR se derrumba en producción mientras ROC se queda clavado, y una transformación de temperatura separa visualmente discriminación de calibración con su reliability diagram, ECE y Brier en vivo (Parte 4).

### ROC y AUC

Cada métrica de la Parte 2 vive a un umbral fijo. En vez de congelarlo, se puede preguntar: ¿qué tan bien ordena el modelo los scores, sin comprometerse con ningún umbral? Es la cualidad "ordenar bien" de 1.2. La curva **ROC** (*Receiver Operating Characteristic*) mide eso.

Se barre el umbral de 1 a 0, anotando en cada posición:

```
TPR (recall) = TP / (TP + FN)
FPR          = FP / (FP + TN)
```

Cada punto (FPR, TPR) resume una matriz de confusión completa; recorrer todos los umbrales traza una curva.

Ordenando las 20 transacciones de Ignasio por score y acumulando TP/FP:

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

De ahí en más las siete legítimas restantes solo empujan FPR de 0.417 a 1.0 sin mover recall, hasta `umbral = 0` en (1, 1).

Tres filas destacadas —`0.50` (recall=0.75, FPR=0.25), `0.66` (recall=0.5, FPR=0.083), `0.36` (recall=1.0, FPR=0.417)— son los tres umbrales de 1.4, ahora tres puntos de la misma curva.

Uniendo todos los puntos, desde (0,0) hasta (1,1), se obtiene la curva ROC. Un modelo perfecto trepa pegado al eje vertical hasta (0,1) y luego recto a (1,1). Un modelo al azar traza la diagonal (0,0)→(1,1).

**AUC** (*area under the curve*) resume la curva en un número: el modelo de Ignasio da AUC ≈ 0.885.

Lectura intuitiva: AUC es la probabilidad de que, tomando una fraudulenta y una legítima al azar, el modelo le dé mayor score a la fraudulenta. De los 8×12=96 pares posibles, en 85 el fraude queda arriba — 85/96 ≈ 0.885. AUC=0.5 es azar puro; AUC=1.0 es separación perfecta.

Importante: AUC no depende de ningún umbral — resume la curva entera. Ideal para comparar modelos ("¿cuál ordena mejor?") sin acordar antes dónde va la perilla.

### La curva Precision–Recall y Average Precision (PR-AUC)

ROC usa FPR, que tiene TN en el denominador — la clase legítima, gigantesca cuando el fraude es raro. La curva **PR** grafica (recall, precision) en su lugar: de las que el modelo marca, ¿cuántas son reales?

Mostrando solo los puntos donde entra un TP nuevo (donde se mueve el recall):

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

(Entre puntos donde solo entra un FP, el recall no se mueve pero precision sigue cayendo.)

Forma típica: empieza arriba a la izquierda y cae hacia la derecha. Con umbral alto casi todo lo señalado es fraude real (precision alta) pero recall bajo; al bajar el umbral, cada fraude nuevo trae más legítimas cruzando la línea, y precision cede — la misma tensión precision-recall, dibujada.

**Average Precision (AP)** promedia la precision en cada punto donde aparece un TP nuevo, ponderada por el salto de recall:

```
AP = Σ (recall_n − recall_(n−1)) · precision_n
```

Con los 8 saltos de 0.125 cada uno:

```
AP = 0.125 · (1.0+1.0+1.0+1.0+0.833+0.75+0.7+0.615) ≈ 0.862
```

Parecido al AUC (0.885) — no es casualidad, resumen la misma familia de curvas. Pero difieren en el punto de referencia: la diagonal de ROC (azar) siempre vale 0.5, sin importar la prevalencia; en PR, un modelo que no distingue nada traza una línea horizontal en `precision = prevalencia` (0.4 aquí), no en 0.5. El "no mejor que el azar" de PR-AUC depende de qué tan común es el fraude; el de ROC-AUC no.

### ROC vs PR (cuál usar cuando la clase positiva es rarísima)

Recall y FPR no cambian con la prevalencia de la población; precision sí, porque mezcla recall, FPR y π (2.5).

La curva ROC está construida solo con TPR y FPR — no depende de π. Así que es *exactamente la misma* en validación balanceada y en producción con 1% de fraude. Suena tranquilizador, pero es la trampa: ROC no se entera de que el problema cambió.

La curva PR sí se entera, porque precision depende de π. Aplicando la fórmula de 2.5 con π=0.01 en vez de 0.4:

| recall | FPR | precision (π=0.4, validación) | precision (π=0.01, producción) |
|---|---|---|---|
| 0.125 – 0.5 | 0 | 1.0 | 1.0 |
| 0.625 | 0.083 | 0.833 | ≈0.070 |
| 0.75 | 0.167 | 0.75 | ≈0.044 |
| 0.875 | 0.25 | 0.7 | ≈0.034 |
| 1.0 | 0.417 | 0.615 | ≈0.024 |

El AP en producción cae de 0.862 a ≈0.52 — mismo modelo, ningún score cambiado. El AUC-ROC sigue clavado en 0.885 — un espejismo de estabilidad.

Regla práctica: cuando la clase positiva es rarísima —fraude, spam, enfermedades raras— **mirar la curva PR (y AP)**, porque refleja lo que de verdad vive el equipo que revisa alarmas. ROC/AUC sirve para comparar el poder de ranking puro entre modelos, sobre todo con clases balanceadas o costos de FP/FN simétricos.

## Parte 4 — ¿Ordena bien, o además le atina a la probabilidad?

### Discriminación vs calibración (AUC mide ranking, no probabilidades creíbles)

En 1.2 se separaron **ordenar bien** (discriminación) y **que el número sea creíble** (calibración). Toda la Parte 3 midió solo la primera. Vale la pena demostrar, con números, que son independientes.

**Discriminación sin calibración.** Tomando el modelo de Ignasio (M1) y aplicando una transformación de "temperatura" que lo hace más extremo:

```
logit(p) = ln(p / (1 − p))
M2(p) = sigmoide(3 · logit(p))
```

Es estrictamente monótona, así que no cambia ningún orden relativo: AUC(M2) = AUC(M1) ≈ 0.885. Pero los valores:

| transacción | score M1 | score M2 (temperatura ×3) |
|---|---|---|
| 0.36 (fraude real) | 0.36 | ≈ 0.15 |
| 0.62 (fraude real) | 0.62 | ≈ 0.81 |
| 0.66 (legítima real) | 0.66 | ≈ 0.88 |

M2 ordena igual, pero como número miente: dice 15% a un fraude real y 88% a una legítima. Mismo ranking, calibración muchísimo peor.

**Calibración sin discriminación.** Un modelo M3 que ignora la entrada y asigna a *toda* transacción la prevalencia observada (`0.4`): en agregado está perfectamente calibrado (40% de las veces que dice 0.4, es fraude), pero no distingue nada — todos los scores empatados, AUC(M3) = 0.5. Calibración perfecta, discriminación nula.

Moraleja: ni AUC ni PR-AUC dicen nada sobre si el número es creíble, y calibración perfecta en agregado no garantiza discriminación. Hacen falta ambas.

### Calibración (reliability diagram, Brier, ECE — cuándo importa)

Calibración: de todas las veces que el modelo dijo *aproximadamente p*, ¿qué fracción resultó fraude de verdad?

**Reliability diagram**: agrupar en baldes por score y comparar el score promedio contra la fracción real de fraude en cada balde. Sobre las 20 transacciones, baldes de ancho 0.25:

| balde de score | n | score promedio (confianza) | fracción real de fraude (observado) |
|---|---|---|---|
| [0.75, 1.0] | 3 | 0.857 | 1.0 |
| [0.50, 0.75) | 6 | 0.600 | 0.5 |
| [0.25, 0.50) | 6 | 0.367 | 0.333 |
| [0, 0.25) | 5 | 0.106 | 0.0 |

Perfectamente calibrado = confianza igual a observado en cada fila (caerían sobre la diagonal). Acá el modelo es levemente subconfiado en el balde alto y levemente sobreconfiado en el medio — desvío leve, nada como M2.

**ECE** (*Expected Calibration Error*) resume el diagrama en un número, ponderado por tamaño de balde:

```
ECE = Σ (n_balde / n_total) · |confianza_balde − observado_balde|
```

`ECE ≈ 0.088` — desvío chico. 0 sería calibración perfecta.

**Brier score**: error cuadrático medio entre score y etiqueta real, sin necesidad de baldes.

```
Brier = (1/n) · Σ (score_i − y_i)²
```

Para Ignasio, Brier ≈ 0.14. El modelo tramposo M3 (siempre `0.4`, calibrado en agregado pero sin discriminación) tiene Brier = 0.24 — peor, porque Brier mezcla discriminación y calibración en un número. Para aislar específicamente "¿es creíble el número?", el reliability diagram y ECE son más limpios.

**¿Cuándo le importa a Ignasio?** Depende de qué se hace con el score:

- Si solo se usa para **ordenar** o **umbralizar una vez**, la calibración casi no importa — solo cuenta la discriminación (AUC/PR-AUC).
- Si se usa para una **pérdida esperada** (ej. `P(fraude) × monto`), la calibración es central: 0.3 y 0.9 deben reflejar una diferencia real de 3×.
- Si se va a **combinar con otros scores** (promedios, Bayes), todos deben significar lo mismo — mezclar uno bien y otro mal calibrado no tiene sentido.
- Si se **muestra directamente a una persona** ("87% de fraude"), un modelo mal calibrado la engaña sistemáticamente aunque ordene perfecto.
- Elegir el umbral óptimo con una matriz de costos (Parte 6) suele asumir que el score aproxima una probabilidad real — buena discriminación con mala calibración puede llevar al umbral equivocado.

Cuando falla la calibración pero la discriminación es buena (caso M2), no hace falta reentrenar: un ajuste posterior *monótono* —Platt scaling o isotonic regression— recalibra los números sin tocar el orden ni el AUC. Es, literalmente, deshacer la transformación de temperatura de M2.
