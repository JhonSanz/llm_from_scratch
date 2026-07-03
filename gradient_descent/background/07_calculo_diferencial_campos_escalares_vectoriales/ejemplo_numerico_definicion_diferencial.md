# La diferencial en acción: ejemplo numérico con el paraboloide

*Apostol, Cálculo Vol. 2, §8.11 — Definición de campo escalar diferenciable y Teorema 8.5*

Objetivo: ver con números el reparto de papeles en

$$f(\mathbf{a}+\mathbf{v}) = f(\mathbf{a}) + T_{\mathbf{a}}(\mathbf{v}) + \|\mathbf{v}\|\,E(\mathbf{a},\mathbf{v}),$$

donde **$\mathbf{a}$ selecciona la transformación** (parámetro congelado) y **$\mathbf{v}$ es su argumento** (variable viva).

**Función:** $f(x,y) = x^2 + y^2$ (paraboloide). **Punto base:** $\mathbf{a} = (1, 2)$.

## Paso 1 — Construir la máquina $T_{\mathbf{a}}$

Las parciales son $D_1 f = 2x$ y $D_2 f = 2y$. Evaluadas en $\mathbf{a}$:

$$D_1 f(\mathbf{a}) = 2, \qquad D_2 f(\mathbf{a}) = 4.$$

Por el Teorema 8.5, la diferencial queda **congelada**:

$$T_{\mathbf{a}}(v_1, v_2) = 2v_1 + 4v_2.$$

Los coeficientes $2$ y $4$ son números fijos — ya no hay $x$ ni $y$ adentro. También queda fijo $f(\mathbf{a}) = 1 + 4 = 5$.

## Paso 2 — Evaluar la máquina en un $\mathbf{v}$ concreto

Con $\mathbf{v} = (0.1,\ 0.2)$:

| Cantidad | Cálculo | Valor |
|---|---|---|
| Verdad: $f(\mathbf{a}+\mathbf{v}) = f(1.1,\ 2.2)$ | $1.21 + 4.84$ | $6.05$ |
| Predicción del plano: $f(\mathbf{a}) + T_{\mathbf{a}}(\mathbf{v})$ | $5 + (2(0.1) + 4(0.2))$ | $6.00$ |
| Error | $6.05 - 6.00$ | $0.05$ |
| $\|\mathbf{v}\|$ | $\sqrt{0.01 + 0.04}$ | $\approx 0.2236$ |
| Coeficiente $E(\mathbf{a},\mathbf{v}) = \text{error}/\|\mathbf{v}\|$ | $0.05 / 0.2236$ | $\approx 0.2236$ |

## Paso 3 — Encoger $\mathbf{v}$ a la mitad: el fenómeno central

Con $\mathbf{v} = (0.05,\ 0.1)$:

- Predicción: $5 + (0.1 + 0.4) = 5.5$. Verdad: $f(1.05,\ 2.1) = 1.1025 + 4.41 = 5.5125$.
- Error $= 0.0125$: el paso se redujo a la **mitad**, el error cayó a la **cuarta parte** ($0.05 \to 0.0125$).
- $E = 0.0125 / 0.1118 \approx 0.1118$: el coeficiente cayó a la mitad, camino a $0$.

El error muere como $\|\mathbf{v}\|^2$, es decir, **más rápido que $\|\mathbf{v}\|$**. Eso es ser $o(\|\mathbf{v}\|)$; eso es ser diferenciable.

### El error exacto, a mano

Para esta función el error se calcula cerrado:

$$f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) - T_{\mathbf{a}}(\mathbf{v}) = (1+v_1)^2 + (2+v_2)^2 - 5 - 2v_1 - 4v_2 = v_1^2 + v_2^2 = \|\mathbf{v}\|^2.$$

El error es *literalmente* $\|\mathbf{v}\|^2$, de modo que $E(\mathbf{a},\mathbf{v}) = \|\mathbf{v}\| \to 0$. La parte lineal se comió los términos de primer orden; lo que sobra es puro segundo orden.

## Paso 4 — La máquina acepta vectores grandes, pero sin garantía

$T_{\mathbf{a}}$ está definida en todo $\mathbb{R}^2$: con $\mathbf{v} = (1, 1)$ da $2 + 4 = 6$, predicción $11$. La verdad es $f(2,3) = 13$: error $= 2$ y $E = 2/\sqrt{2} \approx 1.41$, nada pequeño. El plano existe y se deja evaluar lejos, pero la promesa "$E$ pequeño" de la definición es puramente **local** ($\|\mathbf{v}\| < r$).

## Paso 5 — Otro punto, otra máquina

En $\mathbf{a}' = (0, 1)$: las parciales dan $D_1 f = 0$ y $D_2 f = 2$, así que

$$T_{\mathbf{a}'}(v_1, v_2) = 0 \cdot v_1 + 2v_2$$

— una máquina completamente distinta (ese plano ni se inclina en dirección $x$). No hay relación algebraica entre $T_{(1,2)}$ y $T_{(0,1)}$: cada punto tiene su propio plano tangente. La "derivada global" es un **campo de transformaciones lineales** $\mathbf{a} \mapsto T_{\mathbf{a}}$.

## Síntesis

- **Fijar $\mathbf{a}$** = fabricar la máquina (coeficientes $2$ y $4$).
- **Variar $\mathbf{v}$** = usarla: $T_{\mathbf{a}}$ es lineal en $\mathbf{v}$, nunca en $\mathbf{a}$.
- **Diferenciabilidad** = la promesa de que, con $\mathbf{v}$ pequeños, lo que la máquina no captura (aquí $\|\mathbf{v}\|^2$) es despreciable frente al tamaño del paso.