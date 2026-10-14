# Desbalance de clases

Seguimos con Ignasio y la Empresa Feliz. La clase positiva es `no_interesado`. En validación, 8 de 20 clientes eran `no_interesado` (π = 0.4); en producción, sobre la base de clientes fieles, apenas el 1% lo es (π = 0.01). La prevalencia π se define en [classification_assesment_1.md](classification_assesment_1.md), sección "El base rate / prevalencia".

La pregunta de fondo: **¿siempre es mejor tener las clases balanceadas?** Depende de en qué etapa estemos. Producción, entrenamiento y evaluación son tres casos distintos.

## 1. En producción: π no se elige

La prevalencia es la que hay. Si el 1% de los clientes fieles es `no_interesado`, así es el mundo, y no tiene sentido preguntar si sería mejor otra. π no se mejora, se mide.

## 2. En entrenamiento: balancear puede ayudar, pero tiene costo

Con π = 0.01, el modelo ve 99 `interesado` por cada `no_interesado`. La loss baja casi igual ignorando la clase rara, así que el modelo puede terminar aprendiendo "siempre digo `interesado`" (el modelo perezoso del 99% de accuracy).

Formas de compensarlo:

- **Sobremuestrear** los `no_interesado`: repetirlos o generar ejemplos sintéticos.
- **Submuestrear** los `interesado`: descartar parte de ellos.
- **Pesos en la loss**: que equivocarse con un `no_interesado` cueste más. En PyTorch, `pos_weight` en `BCEWithLogitsLoss`.

**El costo:** el modelo aprende como si el mundo fuera 50/50 y sus scores salen inflados. Un score de `0.8` ya no significa "80% de probabilidad real de `no_interesado`". Puede seguir **ordenando** bien a los clientes (discriminación), pero queda **descalibrado** (Parte 4 de classification_assesment). Para usar esos scores como probabilidades hay que recalibrar o ajustar el umbral con datos que tengan la π real.

**No siempre hace falta:** si hay suficientes ejemplos de la clase rara, el modelo puede aprender bien con el desbalance real, y basta con **mover el umbral**. Suele ser la solución más simple.

## 3. En evaluación: no balancear

Validación y test deben tener **la misma π que producción**. Si Ignasio balancea el test a mano, la precision sale optimista y se derrumba al desplegar el modelo:

```
precision = (recall · π) / (recall · π + FPR · (1 − π))

validación (π = 0.4):   precision ≈ 0.67
producción (π = 0.01):  precision ≈ 0.029
```

Recall y FPR viajan bien entre poblaciones; precision y accuracy no.

## Resumen

| Etapa | ¿Balancear? |
|---|---|
| Producción | No se elige: π es la que hay |
| Entrenamiento | Opcional: ayuda a aprender la clase rara, pero descalibra los scores |
| Validación/test | No: debe reflejar la π real |

> **Balancear es una herramienta de entrenamiento, no una virtud de los datos.** Siempre se evalúa con la π real.

---

## Temas para estudiar después

### Métricas adecuadas para clases desbalanceadas

### Balanced accuracy y macro/micro/weighted averaging

### Matthews Correlation Coefficient (MCC)

### PR-AUC vs ROC-AUC con clase positiva rara

### Random oversampling y random undersampling

### SMOTE y sus variantes (Borderline-SMOTE, ADASYN)

### Undersampling informado (Tomek links, NearMiss, Edited Nearest Neighbours)

### Class weights y cost-sensitive learning

### Focal loss

### Corrección de la probabilidad tras rebalancear (prior shift)

### Recalibración: Platt scaling e isotonic regression

### Elección del umbral según costos del negocio

### Stratified train/test split y stratified k-fold

### Data leakage al sobremuestrear antes de dividir los datos

### Ensembles para desbalance (BalancedRandomForest, EasyEnsemble, RUSBoost)

### Detección de anomalías como alternativa (one-class SVM, Isolation Forest)

### Dataset shift y label shift entre entrenamiento y producción

### Cuántos datos de la clase minoritaria hacen falta realmente
