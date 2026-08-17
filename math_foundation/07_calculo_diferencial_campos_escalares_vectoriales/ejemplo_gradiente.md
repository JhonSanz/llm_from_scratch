# El plano tangente como "zoom": ejemplo con $f(x,y) = x^2 + y^2$

La idea central: el plano tangente lo dibujan **dos ingredientes juntos**, el punto de anclaje $f(a)$ y el gradiente $\nabla f(a)$. Y ese plano no es un objeto nuevo, siempre estuvo determinado por la fórmula de Taylor de primer orden

$$f(a+v) = \underbrace{f(a) + T_a(v)}_{\text{el plano}} + \underbrace{\lVert v \rVert E(a,v)}_{\text{qué tan rápido nos despegamos de él}}$$

## El ejemplo

Tomamos el paraboloide $f(x,y) = x^2 + y^2$ y el punto $a = (1,1)$.

**Ingrediente 1 — el ancla:** $f(a) = 1^2 + 1^2 = 2$. El plano va a pasar por el punto $(1,1,2)$ del espacio.

**Ingrediente 2 — la inclinación:** las parciales son $D_1 f = 2x$ y $D_2 f = 2y$, osea que

$$\nabla f(1,1) = (2,2)$$

Ojo con esto: el gradiente **no vive sobre la superficie, vive en el dominio**. Es un vector de 2D, en el piso, en el plano $xy$. No es una flecha pegada a la ladera en 3D, es una flecha en el mapa que dice "camina en esta dirección y la altura crecerá lo más rápido posible". Aquí apunta en dirección $(1,1)$ (radialmente hacia afuera, lo cual tiene todo el sentido en un paraboloide) y su norma es $\lVert (2,2) \rVert = 2\sqrt{2} \approx 2.83$, que es la pendiente máxima en ese punto. La bajada más empinada es $-\nabla f = (-2,-2)$, apuntando directo al mínimo en el origen: gradient descent literal.

## Ensamblando el plano

Con $v = (x-1, y-1)$, la fórmula de Taylor sin el error nos da

$$z = \underbrace{2}_{f(a)} + \underbrace{(2,2) \cdot (x-1, y-1)}_{\nabla f(a) \cdot v} = 2 + 2(x-1) + 2(y-1) = 2x + 2y - 2$$

Ese es el plano tangente: el ancla lo puso a altura 2 sobre $(1,1)$, y el gradiente le dio la inclinación. Si el gradiente fuera $O$ (punto crítico), el plano existiría igual pero sería horizontal, anclado en $f(a)$, sin inclinación — por eso en puntos críticos no hay dirección privilegiada.

## Verificando el "contrato" del error (la idea del zoom)

La diferenciabilidad promete que cerca de $a$ la superficie y el plano son casi indistinguibles. Comparemos $f$ contra el plano acercándonos en diagonal:

| Punto | $f$ (real) | Plano | Error |
|---|---|---|---|
| $(1.5,\ 1.5)$ | $4.5$ | $4$ | $0.5$ |
| $(1.1,\ 1.1)$ | $2.42$ | $2.4$ | $0.02$ |
| $(1.01,\ 1.01)$ | $2.0402$ | $2.04$ | $0.0002$ |

Cada vez que la distancia se reduce por 10, el error se reduce por **100**: el error es cuadrático en la distancia. Y eso es exactamente lo que exige la definición de diferenciabilidad: el error total es $\lVert v \rVert E(a,v)$, donde el $\lVert v \rVert$ ya es lineal y el $E \to 0$ aporta el decaimiento extra. El error muere *más rápido* que la distancia, y por eso al hacer zoom la superficie "se convierte" en el plano.

En este ejemplo el error se puede calcular exacto:

$$f - \text{plano} = (x-1)^2 + (y-1)^2 = \lVert v \rVert^2$$

osea que $E(a,v) = \lVert v \rVert$, que efectivamente tiende a cero cuando $\lVert v \rVert \to 0$.

## Las derivadas direccionales salen gratis

Por el teorema 8.5 ya no necesitamos ningún límite para calcular derivadas direccionales, solo consultar el gradiente con producto punto:

- Máxima subida, $y = \frac{1}{\sqrt{2}}(1,1)$: $\quad f'(a;y) = (2,2)\cdot\frac{(1,1)}{\sqrt{2}} = 2\sqrt{2}$ — exactamente $\lVert \nabla f \rVert$, como predice la fórmula $f'(a;y) = \lVert \nabla f \rVert \cos\theta$ con $\theta = 0$.
- Perpendicular, $y = \frac{1}{\sqrt{2}}(1,-1)$: $\quad f'(a;y) = 0$ — estamos caminando por la curva de nivel, que aquí es el círculo $x^2 + y^2 = 2$. El gradiente siempre es perpendicular a las curvas de nivel.
- Coordenada, $y = e_1 = (1,0)$: $\quad f'(a;e_1) = 2 = D_1 f(a)$ — las parciales son el caso particular.

Dos números, $(2,2)$, determinan el comportamiento de primer orden de $f$ en **todas** las direcciones desde ese punto. Eso es lo que compramos con el teorema 8.5.

## La imagen del plano inclinado

Con el zoom, las tres propiedades del gradiente se vuelven obvias sin cuentas. En un plano inclinado, dibujando sus líneas horizontales (las de altura constante):

- Caminar **a lo largo** de una línea horizontal → no subes ni bajas. Son las direcciones perpendiculares al gradiente, y proyectadas al piso son las curvas de nivel.
- Caminar **perpendicular** a esas líneas, hacia arriba → la subida más empinada. Esa dirección es el gradiente. Cualquier otra dirección es un "atajo diagonal" que sube menos por paso.
- La misma perpendicular hacia abajo → $-\nabla f$, la bajada más empinada.

El $\cos\theta$ de la fórmula es la interpolación entre esos extremos: caminar en diagonal te da la fracción de la pendiente máxima que corresponde a cuánto tu dirección "se parece" a la perpendicular.

Y como el argumento nunca usó nada de la superficie concreta (solo diferenciabilidad + Cauchy-Schwarz), esto vale para *cualquier* campo escalar diferenciable, en cualquier dimensión: en $\mathbb{R}^2$, en $\mathbb{R}^{100}$, o en el espacio de pesos de una red neuronal con $10^9$ parámetros. La geometría particular de $f$ quedó encapsulada dentro del vector $\nabla f(a)$.

## La inversión conceptual (importante)

En cálculo de una variable, primero se define la derivada como límite del cociente y *después* se demuestra que la recta tangente aproxima bien. En varias variables, Apostol lo hace **al revés**: la definición de diferenciabilidad *es* "existe una fórmula de Taylor de primer orden con error que muere más rápido que $\lVert v \rVert$". La existencia del plano-zoom no es un teorema derivado, es el punto de partida. Todo lo demás (que existan las direccionales, que el gradiente apunte a la máxima subida, que $f$ sea continua — teorema 8.6) son consecuencias de haber *exigido* ese plano de entrada.

Por eso el contraejemplo de §8.10 no es diferenciable: tiene todas sus derivadas direccionales, pero no existe ningún plano que la aproxime uniformemente en todo el entorno. Las direccionales son consultas recta por recta; el plano es una promesa sobre todas las formas de acercarse a la vez.

Esta forma de pensarlo es la que escala: para campos vectoriales $f: \mathbb{R}^n \to \mathbb{R}^m$ la definición será idéntica, con la matriz jacobiana ocupando el asiento de la transformación lineal. "Diferenciable = bien aproximado por algo lineal" es la única definición necesaria de aquí hasta backpropagation.

## Resumen para la memoria

- $f(a)$ → **ancla** el plano (altura).
- $\nabla f(a)$ → lo **inclina** (dirección + magnitud de la pendiente máxima), viviendo en el dominio, no en la superficie.
- $\lVert v \rVert E(a,v)$ → la **letra pequeña del contrato**: qué tan rápido la superficie real se despega del plano al alejarse.

"Diferenciable en $a$" se lee como: *existe un plano que aproxima tan bien a $f$ cerca de $a$ que el error muere más rápido que la distancia* — y el gradiente es la inclinación de ese plano.

**Ejercicio de un minuto:** repetir con $a = (2,0)$. Ahí $\nabla f = (4,0)$ apunta puro en $x$ (radial otra vez) y con norma mayor — la ladera es más empinada lejos del origen.