# El gradiente y la dirección de máximo crecimiento (Apostol §8.12)

## 1. El gradiente

Para un campo escalar $f$ diferenciable en $a$, el gradiente es el vector cuyas componentes son las derivadas parciales:

$$\nabla f(a) = (D_1 f(a), \dots, D_n f(a))$$

Es un **dato de la función**: depende solo de $f$ y del punto $a$. No depende de ninguna dirección elegida — por eso no aparece ningún $y$ en su definición.

La fórmula clave (Teorema 8.5) expresa toda derivada direccional como un producto punto:

$$f'(a; y) = \nabla f(a) \cdot y$$

## 2. Demostración de que diferenciabilidad implica continuidad (Teorema 8.6)

Partiendo de la fórmula de Taylor de primer orden (8.12):

$$|f(a+v) - f(a)| = |\nabla f(a)\cdot v + \|v\|\, E(a,v)|$$

**Paso 1 — Desigualdad triangular** ($|x+y| \le |x| + |y|$), separando los dos sumandos:

$$|f(a+v) - f(a)| \le |\nabla f(a)\cdot v| + \|v\|\,|E(a,v)|$$

**Paso 2 — Cauchy-Schwarz** ($|u \cdot v| \le \|u\|\,\|v\|$), aplicada solo al producto punto:

$$0 \le |f(a+v) - f(a)| \le \|\nabla f(a)\|\,\|v\| + \|v\|\,|E(a,v)|$$

**Paso 3 — Sándwich.** Ambos términos de la cota tienen factor $\|v\|$. Cuando $\|v\| \to 0$:
- $\|\nabla f(a)\|\,\|v\| \to 0$ (el gradiente es constante fijo).
- $\|v\|\,|E(a,v)| \to 0$ (además $E(a,v) \to 0$ por definición de diferenciabilidad).

Por lo tanto $f(a+v) \to f(a)$: continuidad en $a$. $\blacksquare$

**Patrón general:** para acotar una suma, la triangular la parte en pedazos y cada pedazo se ataca con su herramienta (aquí Cauchy-Schwarz para el producto punto).

## 3. La figura 8.5: qué representa cada flecha

- $\nabla f(a)$: vector fijo, determinado por la función.
- $y$: vector **unitario arbitrario**, una dirección que yo elijo. Pudieron dibujar infinitos.
- La llave (corchete): la **proyección** de $\nabla f(a)$ sobre la recta de $y$. Esa "sombra" es exactamente $f'(a;y)$.

La figura muestra a propósito un $y$ **subóptimo**: forma ángulo con el gradiente, así que la proyección es más corta que $\|\nabla f(a)\|$. Si giro $y$ hasta alinearlo con el gradiente, la sombra es el gradiente completo.

## 4. Por qué el gradiente apunta en la dirección de máximo crecimiento

**El problema:** maximizar $f'(a;y) = \nabla f(a) \cdot y$ sobre todos los $y$ unitarios (con $\nabla f(a) \neq 0$).

### Versión algebraica (dos pasos)

**Paso 1 — Cota universal (Cauchy-Schwarz):**

$$f'(a;y) \le |\nabla f(a) \cdot y| \le \|\nabla f(a)\|\,\|y\| = \|\nabla f(a)\|$$

Ninguna dirección puede superar $\|\nabla f(a)\|$. Pero una cota superior no garantiza que se alcance — falta el segundo paso.

**Paso 2 — El techo se alcanza.** Tomando $y^* = \dfrac{\nabla f(a)}{\|\nabla f(a)\|}$:

$$f'(a; y^*) = \nabla f(a) \cdot \frac{\nabla f(a)}{\|\nabla f(a)\|} = \frac{\|\nabla f(a)\|^2}{\|\nabla f(a)\|} = \|\nabla f(a)\|$$

**Unicidad (bonus):** la igualdad en Cauchy-Schwarz ocurre si y solo si los vectores son paralelos, así que $y^*$ es la **única** dirección que alcanza el máximo.

**Estructura lógica del argumento** (patrón recurrente en optimización):
1. Cota que aplica a *todos* los candidatos.
2. Exhibir un candidato que la *alcanza*.

Ninguno de los dos basta solo.

### Versión de Apostol (el $\cos\theta$)

Apostol sí justifica el resultado, pero en una línea comprimida:

$$f'(a;y) = \|\nabla f(a)\|\,\|y\|\cos\theta = \|\nabla f(a)\| \cos\theta$$

El chiste: $\|\nabla f(a)\|$ es constante fija; la **única perilla** que controlo al elegir $y$ es $\cos\theta$. Y del coseno sé que:
1. Su rango es $[-1,1]$ → el techo es $1$ (equivale al Paso 1).
2. Vale $1$ solo cuando $\theta = 0$, o sea $y$ alineado con $\nabla f(a)$ (equivale al Paso 2 + unicidad).

Ambas versiones son el mismo argumento: Cauchy-Schwarz es lo que garantiza que $\frac{u\cdot v}{\|u\|\|v\|} \in [-1,1]$ y por tanto lo que valida definir el "ángulo" en $\mathbb{R}^n$. La versión algebraica funciona en cualquier dimensión sin apelar a dibujos.

## 5. Los tres casos notables, de una sola fórmula

| Ángulo | $\cos\theta$ | Derivada direccional | Interpretación |
|---|---|---|---|
| $\theta = 0$ | $1$ | $\|\nabla f(a)\|$ | Máximo crecimiento (dirección del gradiente) |
| $\theta = 90°$ | $0$ | $0$ | Sin cambio → el gradiente es ⊥ a las curvas de nivel |
| $\theta = 180°$ | $-1$ | $-\|\nabla f(a)\|$ | Máximo decrecimiento (dirección opuesta) |

**Precisión de lenguaje:** el gradiente no apunta hacia el máximo global de la función; apunta hacia donde la subida es más empinada *localmente en ese punto*. Como en la montaña: el paso más empinado bajo mis pies no necesariamente mira a la cima.

**Nota:** la norma del gradiente no es decorativa — $\|\nabla f(a)\|$ **es** la tasa máxima de crecimiento.

## 6. Conexión con el roadmap (LLMs)

El descenso de gradiente en machine learning se mueve en la dirección $-\nabla f$ precisamente por el caso $\cos\theta = -1$: es la dirección de máximo decrecimiento de la función de pérdida. El argumento cota + candidato es el que sobrevive en espacios de parámetros de dimensión enorme, donde ya no hay ángulos que dibujar.