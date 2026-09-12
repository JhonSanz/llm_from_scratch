# Cheatsheet — Diagnóstico y mediciones para clasificación

Referencia rápida de `classification_assesment_1.md`. Ejemplo base: 20 transacciones de Ignasio (8 fraude, 12 legítimas), umbral `0.5` → **6 TP, 3 FP, 2 FN, 9 TN**.

## Parte 1 — Cimientos

| Concepto | Definición | Idea clave |
|---|---|---|
| **Real distribution (D)** | Universo completo de ejemplos posibles | Nunca se tiene acceso completo |
| **Sample (S)** | Muestra finita de D (train/val) | Lo único que el modelo "ve" |
| **Empirical risk** | Error sobre S | Bajo esto no implica generalizar |
| **True risk** | Error sobre D completo | Lo que de verdad importa; `test data` lo estima |
| **Generalizar** | Lograr true risk bajo, no solo empirical risk | Memorizar S ≠ entender D |
| **Score** | Número en `[0,1]`, salida cruda del modelo | No es una decisión |
| **Decisión** | `score ≥ umbral` → clase positiva | Post-proceso, arbitrario, se puede cambiar sin reentrenar |
| **Discriminación** | ¿Ordena bien fraudes por encima de legítimas? | Independiente de calibración — mide ROC/PR |
| **Calibración** | ¿El número es una probabilidad creíble? | Independiente de discriminación — mide reliability/ECE/Brier |

> Un score puede tener una cualidad sin la otra (ver Parte 4).

## Parte 1.3–1.4 — Matriz de confusión y umbral

| | Real: Fraude | Real: Legítima |
|---|---|---|
| **Predicho: Fraude** | TP (acierto) | FP (falsa alarma) |
| **Predicho: Legítima** | FN (fraude escapado) | TN (acierto) |

- **Umbral** es una perilla — moverla reacomoda TP/FP/FN/TN por completo, sin tocar el modelo.
- Umbral ↓ → más TP y más FP (↑ recall, ↓ precision). Umbral ↑ → lo opuesto.
- Nunca reportar una métrica de un solo punto sin decir a qué umbral se midió.

## Parte 2 — Métricas a UN umbral fijo

| Métrica | Fórmula | Pregunta que responde | Punto ciego / trampa |
|---|---|---|---|
| **Precision** | `TP/(TP+FP)` | De las alarmas, ¿cuántas son reales? | Se derrumba con clases raras (ver base rate). Modelo que casi nunca actúa puede tener precision=1 sin atrapar nada. |
| **Recall (= sensitivity = TPR)** | `TP/(TP+FN)` | De los fraudes reales, ¿cuántos atrapó? | No depende de la prevalencia. Modelo que marca todo tiene recall=1 sin servir de nada. |
| **FPR** (*false positive rate*) | `FP/(FP+TN)` | De las legítimas reales, ¿a cuántas les disparó una falsa alarma? | Métrica de pleno derecho, espejo exacto de recall sobre la otra columna de la matriz (1.3). No depende de la prevalencia. Complemento `1−FPR` = **specificity**. Reaparece como eje x de ROC (Parte 3) y como ingrediente de precision vs π (siguiente sección). |
| **F1** | `2·P·R/(P+R)` (media armónica) | Resumen de P y R en un solo número | Sigue dependiendo del umbral; pesa igual FP y FN (ver F-beta si no). Media aritmética (P+R)/2 es una trampa — deja que un valor alto tape a uno bajo. |
| **Accuracy** | `(TP+TN)/total` | ¿Qué fracción acertó, en general? | Antipatrón con clases desbalanceadas — un modelo que siempre dice "legítima" puede dar 99% accuracy y 0 fraude detectado. |

**Tensión precision–recall**: TP y FP viven del mismo lado de la línea del umbral → moverla afecta a ambos. No existe umbral que maximice las dos a la vez (salvo separación perfecta). Por eso comparar modelos con una sola métrica a un umbral es tramposo.

### Base rate / prevalencia — π

```
prevalencia = (TP+FN) / total
precision = (recall·π) / (recall·π + FPR·(1−π))     ← igual al teorema de Bayes
```

- `recall` y `FPR` **no dependen de π** — son propiedades del modelo a un umbral dado.
- `precision` **sí depende de π** — mezcla recall, FPR y prevalencia.
- Umbral=0 (marca todo): `precision → π`, el piso absoluto de cualquier modelo.
- **Lección**: precision medido en validación balanceada no se transfiere a producción con clase rara. Recall sí viaja razonablemente bien.

## Parte 3 — Métricas que barren TODOS los umbrales

| Curva | Ejes | Métrica resumen | Qué mide |
|---|---|---|---|
| **ROC** | FPR (x) vs TPR/recall (y) | **AUC** | Probabilidad de que un fraude al azar reciba mayor score que una legítima al azar. No depende de π. |
| **PR** | Recall (x) vs Precision (y) | **AP** (average precision) | `Σ (recall_n − recall_{n−1}) · precision_n`, sumado en cada TP nuevo. Sí depende de π. |

- Diagonal ROC (azar) = siempre 0.5, sin importar π.
- Línea base PR (azar) = `precision = π` (horizontal), **sí** depende de π.
- Un modelo perfecto en ROC: pega al eje vertical hasta (0,1) y luego a (1,1).

### ROC vs PR — cuál usar

| Situación | Usar |
|---|---|
| Clases razonablemente balanceadas, costo FP≈FN | **ROC/AUC** — compara ranking puro |
| Clase positiva rarísima (fraude, spam, enfermedad rara) | **PR/AP** — refleja la experiencia real (cuántas alarmas son reales) |

> ROC-AUC puede quedarse alto y estable mientras PR-AUC se derrumba en silencio al pasar de validación a producción — mismo modelo, mismo umbral, solo cambió π.

## Parte 4 — Discriminación vs calibración (a fondo)

- **Discriminación sin calibración**: transformación monótona de "temperatura" (`sigmoide(T·logit(p))`) no cambia ningún orden → AUC idéntico, pero los números se vuelven mentirosos (un fraude real puede pasar de "dice 36%" a "dice 15%").
- **Calibración sin discriminación**: modelo que siempre predice la prevalencia (ej. `0.4`) → calibrado en el agregado, pero AUC = 0.5 (todos los scores empatan, no distingue nada).
- Arreglo cuando la discriminación es buena pero la calibración falla: **Platt scaling** o **isotonic regression** — ajuste posterior *monótono*, no toca el AUC.

### Herramientas de calibración

| Herramienta | Qué hace | Fórmula |
|---|---|---|
| **Reliability diagram** | Agrupa en baldes de score; compara confianza promedio vs fracción real de fraude por balde | — |
| **ECE** (Expected Calibration Error) | Resume el diagrama en un número | `Σ (n_balde/n_total)·\|confianza−observado\|` |
| **Brier score** | Error cuadrático medio score vs etiqueta — mezcla discriminación y calibración, no aísla solo una | `(1/n)·Σ(score_i − y_i)²` |

### ¿Cuándo importa la calibración?

- Solo se **ordena** o se **umbraliza una vez**: no importa, con discriminación alcanza.
- Se calcula una **pérdida esperada** (`P(fraude) × monto`): calibración es central.
- El score se **combina con otros** (promedio, Bayes): todos deben significar lo mismo.
- El score se **muestra a una persona** como probabilidad: mal calibrado = engaño sistemático.
- Elegir umbral óptimo con **matriz de costos** (Parte 6): asume que el score aproxima una probabilidad real.

## Regla de oro general

> Ninguna métrica puntual (precision, recall, F1, accuracy) tiene sentido sin decir **a qué umbral** y **a qué prevalencia** se midió. Para comparar modelos sin comprometerse a ninguno de los dos, usar AUC/AP — y para saber si el número en sí es honesto, calibración (reliability/ECE/Brier), por separado del ranking.

---
*Ver simuladores interactivos: [html/score_umbral_metricas_prevalencia.html](html/score_umbral_metricas_prevalencia.html) (Parte 1-2) y [html/roc_pr_calibracion.html](html/roc_pr_calibracion.html) (Parte 3-4).*
