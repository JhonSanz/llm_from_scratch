

## Parte 5 — El mundo de verificación / detección

### Clasificación vs verificación   (por qué este bloque es OTRO setting, no fraude)
### FAR, FRR y EER
### DET curve

## Parte 6 — De la métrica a la decisión de negocio

### Matriz de costos   (un FN y un FP no cuestan lo mismo)
### Selección de umbral   (Youden's J, target de recall, mínimo costo esperado)

## Parte 7 — Cuando hay más de dos clases 

### Matriz de confusión multiclase
### Micro, macro y weighted averaging

## Parte 8 — Métricas resumen de una sola cifra

### MCC (Matthews) y kappa de Cohen   (por qué se portan mejor que F1 bajo desbalance)

## Parte 9 — ¿Está aprendiendo o memorizando?

### Overfitting y generalización
### Bias–variance   (las dos caras del mismo error)

## Parte 10 — Metodología de evaluación (transversal a todo lo anterior)

### Splits: train / validation / test
### Cross-validation y stratified k-fold
### GroupKFold
### Split temporal
### Data leakage   (target, temporal, de grupo, de preprocesamiento)
### Nested CV   (elegir hiperparámetros sin contaminar el test)

## Parte 11 — ¿La mejora es real o es ruido?

### Incertidumbre: intervalos de confianza por bootstrap
### Comparar dos modelos: test de McNemar

## Parte 12 — Después de que Ignasio despliega

### Drift y monitoreo en producción   (concept drift, PSI, re-evaluación en el tiempo)