# Diagnóstico y mediciones para algoritmos de ML de clasificación

Supongamos un investigador/ingeniero ML llamado Ignasio en una empresa ficticia llamada la "Empresa Feliz". Ignasio tiene la tarea de entrenar un modelo que clasifique correctamente transacciones como fraudulentas o legítimas.

Para ello se le suministran permisos de acceso en base de datos para consultar transacciones historicas. Ignasio está feliz porque usó pytorch para crear su MLP con el módulo `n.n`, sin embargo después de un entrenamiento de varios días con su pc encendido consumiendo electricidad con su RTX 5070 viene una pregunta muy importante y fundamental: **¿Esto si está aprendiendo al clasificar?**

Específicamente, los algoritmos de clasificación como los MLP, random forest, SVM etc tiene una clara función y es que basado en los datos de entrenamiento, los "engranajes internos" del algoritmo se acomodan para **generalizar** los datos, y ante uno nuevo totalmente desconocido es capaz de reconocer los patrones y decir a qué categoría es propable que pertenezca

Por lo cual, lo que sigue son los conceptos fundamentales y mas importantes para concluir si Ignasio está haciendo bien su trabajo y no será despedido de la Empresa Feliz

## Parte 1 — Los cimientos

### ¿Qué significa "generalizar"?

En la "Escuela Feliz" dos estudiantes de octavo grado cursan por primera vez álgebra 1, una materia que suele ser retadora para todos los estudiantes. El estudiante A tiene la costumbre de aprenderse de memoria todos los ejercicios que el profesor propone, mientras que el estudiante W intenta entender el por qué de todos los procesos y trucos aritméticos que se enseñan en la clase

El día del examen del primer corte el profesor usa preguntas de talleres que envió a los estudiantes durante las semanas previas al examen. En este caso, ambos el estudiante A y W aprueban con una nota alta. Sin embargo, para el segundo corte el profesor decide usar algunas preguntas nuevas que ningún estudiante ha visto, pero que conservan el espíritu y los mecanismos de otros ejemplos compartido en los talleres

Podemos imaginar el resultado, cuando el estudiante A ve las preguntas nuevas no puede resolverlas y repureba el examen. El estudiante W entiende el por qué de todo y logra responder la mayoría bien, aprobando.

Vale la pena mencionar que si el profesor evaluara cálculo integral en vez de álgebra, ni siquiera W aprobaría, y no sería justo llamarlo "mala generalización".

---
Usando la terminología técnica, existe una **real distribution** (distribución real) de problemas de álgebra —llamémosla *D*— que contiene todos los ejercicios posibles del universo del álgebra 1, tanto los que ya se resolvieron en clase como los que jamás se han planteado. Ni el estudiante A ni el estudiante W tienen acceso a *D* completa; lo único que vieron fueron los talleres de las semanas previas, es decir, un **sample** (muestra finita) de esa distribución que llamaremos *S*.

Cuando el estudiante A se aprende de memoria los ejercicios de los talleres, está minimizando su error sobre *S*, sobre la muestra que sí tuvo enfrente. A eso se le llama **empirical risk** (riesgo empírico): qué tan seguido se equivoca en los ejemplos que ya conoce. Y por eso en el primer corte le va bien, porque el profesor evaluó justamente con preguntas sacadas de *S*.

Pero lo que de verdad mide si alguien aprendió álgebra no es *S*, sino *D*: la capacidad de responder cualquier ejercicio del universo entero, incluidos los que nunca vio. Ese es el **true risk** (riesgo verdadero), el error sobre toda la distribución. El estudiante W lo tiene bajo porque entendió los mecanismos de fondo; el estudiante A lo tiene por las nubes, aunque su empirical risk fuera casi cero.

**Generalizar es lograr que el true risk sea bajo, y no solo el empirical risk.** El segundo corte —con preguntas nuevas que conservan el espíritu de los talleres— es precisamente un intento del profesor de estimar el true risk: tomar una segunda muestra que el estudiante no vio y usarla para descubrir quién entendió y quién solo memorizó. Ese es, exactamente, el papel que van a cumplir los **test data** (datos de prueba) con el modelo de Ignasio.


### El objeto que medimos es un *score*, no una decisión

Recordando un poco la regresión logística y los análisis que hicimos, vimos que el objetivo de todo fue decir "el ejemplo tiene X probabilidad de pertenecer a la clase A", teniendo en cuenta la frontera de decisión, la cual tenia una influencia directa con la función sigmoide, después de ajustar la recta lográbamos aplanar con la sigmoide y obtener la probabilidad

El problema es que `0.5` desde la probabilidad no nos clasifica nada. Entonces, cual es la diferencia entre tener un ejemplo con score `0.51` y otro `0.9`? ambos están por encima del umbral para considerar que "es mas probable que pertenezca a la clase A". Sin embargo el modelo está obviamente mas convencido de la segunda, y es por eso que debemos valorar ese "nivel de convencimiento"

Así que la solución es poner un valor para decir "de aquí para allá lo considero fraude"

El score tiene dos cualidades que son totalmente independientes entre sí:

- **Ordenar bien**: ¿el modelo tiende a darles score más alto a los fraudes de verdad que a las transacciones legítimas?, no importa el valor exacto, importa el orden.
- **Que el número sea una probabilidad creíble**: si el modelo dice 0.8, ¿de verdad alrededor de 8 de cada 10 de esos casos resultan ser fraude?


### La matriz de confusión: TP, FP, FN, TN
### El umbral de decisión es una perilla, no un dato

## Parte 2 — Métricas a UN umbral fijo (un punto)

### Precision
### Recall
### La tensión precision–recall   (por qué no podés maximizar las dos)
### F1   (y por qué media armónica y no promedio normal)
### Accuracy y por qué miente con clases desbalanceadas
### El base rate / prevalencia   (por qué precision se mueve con la prevalencia y recall no)

## Parte 3 — Métricas que barren TODOS los umbrales (una curva)

### ROC y AUC
### La curva Precision–Recall y Average Precision (PR-AUC)
### ROC vs PR   (cuál usar cuando la clase positiva es rarísima — tu caso)

## Parte 4 — ¿Ordena bien, o además le atina a la probabilidad?

### Discriminación vs calibración   (AUC mide ranking, no probabilidades creíbles)
### Calibración   (reliability diagram, Brier, ECE — cuándo importa)

## Parte 5 — El mundo de verificación / detección (tu proyecto de voz)

### Clasificación vs verificación   (por qué este bloque es OTRO setting, no fraude)
### FAR, FRR y EER
### DET curve

## Parte 6 — De la métrica a la decisión de negocio

### Matriz de costos   (un FN y un FP no cuestan lo mismo)
### Selección de umbral   (Youden's J, target de recall, mínimo costo esperado)

## Parte 7 — Cuando hay más de dos clases (tu clasificador de géneros)

### Matriz de confusión multiclase
### Micro, macro y weighted averaging   (dónde vive tu "recall de bambuco")

## Parte 8 — Métricas resumen de una sola cifra

### MCC (Matthews) y kappa de Cohen   (por qué se portan mejor que F1 bajo desbalance)

## Parte 9 — ¿Está aprendiendo o memorizando?

### Overfitting y generalización
### Bias–variance   (las dos caras del mismo error)

## Parte 10 — Metodología de evaluación (transversal a todo lo anterior)

### Splits: train / validation / test
### Cross-validation y stratified k-fold
### GroupKFold   (split por canción, no por clip — ya lo intuías)
### Split temporal   (fraude no se baraja: validás en el futuro)
### Data leakage   (target, temporal, de grupo, de preprocesamiento)
### Nested CV   (elegir hiperparámetros sin contaminar el test)

## Parte 11 — ¿La mejora es real o es ruido?

### Incertidumbre: intervalos de confianza por bootstrap
### Comparar dos modelos: test de McNemar

## Parte 12 — Después de que Ignasio despliega

### Drift y monitoreo en producción   (concept drift, PSI, re-evaluación en el tiempo)