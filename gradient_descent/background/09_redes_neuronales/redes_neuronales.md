Es importante recordar algunas cosas fundamentales de logistic regression que aprendimos hace unos estudios atrás

- **Decision boundary**: usábamos un linea recta, la cual separaba los datos en dos categorías
- **hypotesis**: usábamos la función sigmoide y nos decía la probabilidad de que un ejemplo de entrenamiento perteneciera a una clase
- **cost function**: después de hacer un análisis extenso nos dimos cuenta de que mínimos cuadrados no safisfacía nuestros deseos ya que no castigaba lo suficiente a los ejemplos mal clasificados, por lo tanto se introdujo la función `log loss`

algo que no mencionamos en el estudio de la regresion logística es que la frontera de decisión no necesariamente debe ser una recta. Si introducimos nuevos parámetros podemos lograr "formas" diferentes de trazar la frontera

<agregar ejemplo aqui>

sin embargo esto no es tan facil porque habría que conocer muy bien los datos, y asumimos un costo computacional enorme al tener esa redundancia. Es aquí donde las redes neuronales tienen especial importancia ya que tienen la capacidad de inferir la "curvatura de los datos" sin tener entradas "forzadas" redundantes


# Redes Neuronales

Ya vimos que con logistic regression podemos trazar una frontera de decisión **lineal** ($\theta^T x$) y pasarla por la función sigmoide para obtener una probabilidad. El problema es que muchos datasets no son separables con una sola recta (por ejemplo un dataset en forma de dona, o el clásico problema XOR). Las redes neuronales resuelven esto **encadenando varias regresiones logísticas** para construir fronteras de decisión no lineales.

La idea clave, y la que vamos a rescatar de logistic regression, es esta:

> **Una neurona es, literalmente, una regresión logística.**

Lo que cambia es que ahora vamos a conectar muchas de estas unidades entre sí, organizadas en capas.

### Notación de capas

Vamos a nombrar las capas con el superíndice $(l)$.

- Capa 1 ($a^{(1)}$): es la capa de entrada, es decir, nuestro $x$ de siempre.
- Capas intermedias ($a^{(2)}, a^{(3)}, \dots$): son las capas ocultas ("hidden layers").
- Última capa ($a^{(L)}$): es la capa de salida, lo que antes llamábamos $h_\theta(x)$.

$a_i^{(l)}$ es la "activación" (el valor de salida, después de aplicar la sigmoide) de la unidad $i$ en la capa $l$.

$\Theta^{(l)}$ es la matriz de pesos que controla el mapeo de la capa $l$ a la capa $l+1$. Fíjate que ya no es un vector $\theta$ como en logistic regression, sino una **matriz**, porque cada neurona de la capa $l+1$ necesita su propio vector de pesos para combinar todas las activaciones de la capa $l$.

Igual que agregamos $x_0 = 1$ (el sesgo) en logistic regression, aquí cada capa (excepto la de salida) agrega una unidad de sesgo $a_0^{(l)} = 1$.

### ¿Cuál es la hipótesis?

Tomemos una red pequeña: 3 entradas, una capa oculta de 3 neuronas, y 1 salida.

Para calcular la activación de cada neurona de la capa oculta hacemos exactamente lo mismo que hacíamos para calcular $h_\theta(x)$ en logistic regression: una combinación lineal de las entradas, pasada por la sigmoide.

$$z^{(2)} = \Theta^{(1)} a^{(1)}$$

$$a^{(2)} = g(z^{(2)})$$

donde $g$ es la misma función sigmoide de siempre, $g(z) = \frac{1}{1+e^{-z}}$, aplicada elemento a elemento.

Explícitamente, cada neurona de la capa oculta es una regresión logística que recibe como entrada el vector $x$ completo:

$$a_1^{(2)} = g(\Theta_{10}^{(1)} x_0 + \Theta_{11}^{(1)} x_1 + \Theta_{12}^{(1)} x_2 + \Theta_{13}^{(1)} x_3)$$

$$a_2^{(2)} = g(\Theta_{20}^{(1)} x_0 + \Theta_{21}^{(1)} x_1 + \Theta_{22}^{(1)} x_2 + \Theta_{23}^{(1)} x_3)$$

$$a_3^{(2)} = g(\Theta_{30}^{(1)} x_0 + \Theta_{31}^{(1)} x_1 + \Theta_{32}^{(1)} x_2 + \Theta_{33}^{(1)} x_3)$$

Cada fila de $\Theta^{(1)}$ es, ni más ni menos, un vector $\theta$ como el que usábamos en logistic regression. La diferencia es que ahora tenemos **tres fronteras de decisión lineales en paralelo** en lugar de una sola.

Y para llegar a la salida repetimos el mismo paso, pero ahora usando las activaciones de la capa oculta como "features" de entrada:

$$z^{(3)} = \Theta^{(2)} a^{(2)}$$

$$h_\Theta(x) = a^{(3)} = g(z^{(3)})$$

$$h_\Theta(x) = g(\Theta_{10}^{(2)} a_0^{(2)} + \Theta_{11}^{(2)} a_1^{(2)} + \Theta_{12}^{(2)} a_2^{(2)} + \Theta_{13}^{(2)} a_3^{(2)})$$

Este proceso de ir calculando $a^{(2)}, a^{(3)}, \dots$ hacia adelante se llama **forward propagation**.

Vale la pena recalcar que si nuestra red tiene unicamente una salida, para esa neurona la matriz $\Theta$ se reduce a un vector. Encontraremos otra matriz $\Theta$ en la última capa para el caso de una red con varias salidas, ya que allí se solapan los vectores generando la matiz

> **La hipótesis de una red neuronal es una composición de regresiones logísticas.** Cada capa aprende sus propias "fronteras de decisión lineales" sobre la salida de la capa anterior, y al combinarlas se pueden formar fronteras de decisión no lineales y arbitrariamente complejas.

En general, para pasar de la capa $l$ a la $l+1$:

$$z^{(l+1)} = \Theta^{(l)} a^{(l)} \qquad a^{(l+1)} = g(z^{(l+1)})$$

con $a^{(1)} = x$, y $h_\Theta(x) = a^{(L)}$ en la última capa.


### Ejemplo numérico: de $x$ a $a^{(2)}$ paso a paso

Un ejemplo con números chiquitos que puedes verificar a mano, para no volver a confundir el producto matriz-vector con la sigmoide. Usamos una capa oculta de 3 neuronas, con 2 entradas reales más el sesgo (justo como en la sección anterior).

#### El montaje

Entrada, con el sesgo $x_0 = 1$ adelante:

$$x = a^{(1)} = \begin{bmatrix} x_0 \\ x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$$

Matriz de pesos de la primera capa. Tiene **3 filas** (una por neurona) y **3 columnas** (una por entrada, incluido el sesgo):

$$\Theta^{(1)} = \begin{bmatrix} 0 & 0.5 & 1 \\ 1 & 1 & 1 \\ -1 & 0 & 1 \end{bmatrix} \begin{matrix} \leftarrow \text{neurona 1} \\ \leftarrow \text{neurona 2} \\ \leftarrow \text{neurona 3} \end{matrix}$$

#### Paso 1 — producto matriz-vector $\Rightarrow$ da el vector $z^{(2)}$

Las dimensiones ya anticipan que sale un vector: $(3\times 3)\cdot(3\times 1) = (3\times 1)$. Cada componente del resultado es el **producto punto de una fila con $x$**:

$$
\begin{aligned}
z_1^{(2)} &= (0)(1) + (0.5)(2) + (1)(-1) = 0 + 1 - 1 = 0 \\
z_2^{(2)} &= (1)(1) + (1)(2) + (1)(-1) = 1 + 2 - 1 = 2 \\
z_3^{(2)} &= (-1)(1) + (0)(2) + (1)(-1) = -1 + 0 - 1 = -2
\end{aligned}
$$

Eso es *todo* el producto matriz-vector: tres productos punto hechos de golpe. El resultado es el vector de **pre-activaciones**:

$$z^{(2)} = \Theta^{(1)} x = \begin{bmatrix} 0 \\ 2 \\ -2 \end{bmatrix}$$

> Ojo: esto **todavía no** son los valores de las neuronas. Es $z$, lo crudo. Falta la sigmoide.

#### Paso 2 — sigmoide elemento a elemento $\Rightarrow$ da el vector $a^{(2)}$

Aplico $g(z) = \dfrac{1}{1+e^{-z}}$ a **cada componente por separado**:

$$
a^{(2)} = g\big(z^{(2)}\big) =
\begin{bmatrix} g(0) \\ g(2) \\ g(-2) \end{bmatrix} =
\begin{bmatrix} 0.500 \\ 0.881 \\ 0.119 \end{bmatrix}
$$

**Ahora sí**: ese vector $a^{(2)}$ son las activaciones — los valores de salida de las 3 neuronas de la capa oculta.

#### Lo que hay que grabarse

El proceso es siempre dos pasos, en este orden:

$$x \;\xrightarrow{\;\Theta^{(1)}x\ \ (\text{matriz-vector})\;}\; z^{(2)} \;\xrightarrow{\;g(\cdot)\ \ (\text{elemento a elemento})\;}\; a^{(2)}$$

El producto matriz-vector da un **vector** ($z$), porque la matriz tiene varias filas; la sigmoide luego lo convierte, componente a componente, en las activaciones ($a$).

Ese $a^{(2)} = [0.5,\ 0.881,\ 0.119]$ es ahora la "entrada" de la siguiente capa: repetirías $z^{(3)} = \Theta^{(2)} a^{(2)}$ y otra sigmoide, y así hasta la salida. Mismo par de pasos, una y otra vez.

### ¿Cuál es la función de costo?

Recordemos la función de costo de logistic regression (log loss):

$$J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]$$

Para redes neuronales usamos exactamente la misma idea, con dos generalizaciones:

**1. Puede haber varias unidades de salida.** Si en vez de clasificar en 2 categorías clasificamos en $K$ categorías, la capa de salida tiene $K$ neuronas, y $h_\Theta(x) \in \mathbb{R}^K$. Entonces sumamos el log loss sobre cada una de esas $K$ salidas:

$$J(\Theta) = -\frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} \left[ y_k^{(i)} \log(h_\Theta(x^{(i)}))_k + (1 - y_k^{(i)}) \log(1 - (h_\Theta(x^{(i)}))_k) \right]$$

Es literalmente $K$ regresiones logísticas evaluadas en paralelo, una por cada categoría de salida, y luego promediadas. Con $K=1$ esta fórmula colapsa exactamente a la de logistic regression.

**2. Regularización sobre todos los pesos.** Como ahora tenemos muchas más $\Theta$ (una matriz por cada par de capas), se le suele agregar un término de regularización que penaliza pesos muy grandes (sin penalizar los sesgos $\Theta_{i0}^{(l)}$):

$$J(\Theta) = -\frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} \left[ y_k^{(i)} \log(h_\Theta(x^{(i)}))_k + (1 - y_k^{(i)}) \log(1 - (h_\Theta(x^{(i)}))_k) \right] + \frac{\lambda}{2m} \sum_{l=1}^{L-1} \sum_{i} \sum_{j} \left( \Theta_{ji}^{(l)} \right)^2$$

Igual que antes, entre más cerca de cero esté $J(\Theta)$, mejor está clasificando la red. Y la manera de optimizar $\Theta$ sigue siendo gradient descent, solo que la derivada $\frac{\partial J(\Theta)}{\partial \Theta_{ij}^{(l)}}$ ya no se calcula de un solo paso como en logistic regression, sino propagando el error hacia atrás capa por capa (**backpropagation**), aplicando la regla de la cadena repetidamente sobre la derivada de la sigmoide $g'(z) = g(z)(1-g(z))$ que ya dedujimos. Veamos exactamente qué significa eso en términos de Jacobianas.

### Backpropagation es la regla de la cadena de Jacobianas

En autograd.md vimos dos ideas que parecían abstractas: que la Jacobiana de una composición es el producto de las Jacobianas locales ($D_{G\circ F}(a)=D_G(F(a))\cdot D_F(a)$), y que cuando un nodo alimenta a varias ramas (fan-out), su gradiente hacia atrás es la **suma** de lo que baja por cada rama. La red neuronal que acabamos de definir es exactamente ese tipo de grafo. No hace falta ninguna maquinaria nueva, solo aplicar lo mismo.

#### Forward prop, releído como composición

$$x=a^{(1)} \xrightarrow{\ \Theta^{(1)}\ } z^{(2)} \xrightarrow{\ g\ } a^{(2)} \xrightarrow{\ \Theta^{(2)}\ } z^{(3)} \xrightarrow{\ g\ } a^{(3)}=h_\Theta(x) \xrightarrow{\ \text{log loss}\ } J$$

Cada flecha es un eslabón, y $J$ es la composición de todos ellos. La regla de la cadena de autograd.md aplica sin cambios: la Jacobiana de $J$ respecto a $x$ (o respecto a cualquier $\Theta^{(l)}$) es el producto de las Jacobianas locales de cada eslabón, evaluadas en los valores que forward prop ya calculó.

#### Las dos Jacobianas locales ya las conocemos

Lo bonito es que en una red neuronal solo hay dos tipos de eslabón, y a los dos ya les sacamos la Jacobiana en autograd.md:

1. $z^{(l+1)}=\Theta^{(l)}a^{(l)}$ es una **transformación lineal**. En "Jacobiana en un punto" vimos que la Jacobiana de $y=Ax$ es la propia matriz $A$, en cualquier punto. Entonces, sin derivar nada:

$$D\big(z^{(l+1)}\big)\big/D\big(a^{(l)}\big) = \Theta^{(l)}$$

2. $a^{(l+1)}=g(z^{(l+1)})$ aplica la sigmoide **elemento a elemento**, igual que $f_1(x)=(x_1^2,x_2^2)$ en el ejemplo del fan-out. La Jacobiana de una función elemento a elemento siempre es diagonal, porque $\partial g(z_i)/\partial z_j=0$ cuando $i\neq j$:

```math
D\big(a^{(l+1)}\big)\big/D\big(z^{(l+1)}\big) = \text{diag}\big(g'(z_1^{(l+1)}),\dots,g'(z_{n}^{(l+1)})\big)
```

usando la misma $g'(z)=g(z)(1-g(z))$ de siempre. Con estas dos piezas —matriz de pesos y diagonal de derivadas de sigmoide— se arma la Jacobiana de toda la red, capa por capa, igual que armamos $Dh=Df\cdot Dg$ en autograd.md.

#### Multiplicar Jacobianas de atrás hacia adelante

Como con Karpathy, no conviene expandir $h_\Theta(x)$ completo (eso es *expression swell*): conviene multiplicar Jacobianas locales de atrás hacia adelante, acumulando el producto. Llamemos $\delta^{(l)}=\dfrac{\partial J}{\partial a^{(l)}}$ al vector fila —la Jacobiana de $J$ respecto a la capa $l$, el mismo tipo de objeto que $\partial L/\partial u$ en el ejemplo del fan-out—.

En la capa de salida, $\delta^{(L)}$ sale directo de derivar el log loss respecto a $h_\Theta(x)=a^{(L)}$. Para las capas anteriores, se multiplica por las dos Jacobianas locales de arriba:

$$\delta^{(l)} = \delta^{(l+1)}\cdot \text{diag}\big(g'(z^{(l+1)})\big)\cdot \Theta^{(l)}$$

Escrito en la notación clásica (vector columna, con $.*$ para el producto elemento a elemento en vez de multiplicar por la diagonal), esto es exactamente

$$\delta^{(l)} = \big(\Theta^{(l)}\big)^T\delta^{(l+1)}\ .*\ g'(z^{(l)})$$

la misma ecuación, transpuesta. La $\big(\Theta^{(l)}\big)^T$ que tanta gente memoriza sin saber de dónde sale es, literalmente, la Jacobiana de la capa lineal, usada en la dirección hacia atrás.

#### Y acá aparece el fan-out, otra vez

¿Por qué el backward es una multiplicación matricial y no una suma suelta? Porque cada neurona $a_j^{(l)}$ no alimenta a una sola neurona de la capa $l+1$: alimenta a **todas**, porque $\Theta^{(l)}$ es una matriz densa (cada fila combina las $a_j^{(l)}$ completas, como vimos explícitamente con $a_1^{(2)}, a_2^{(2)}, a_3^{(2)}$ arriba). Es el mismo fan-out del nodo $u$ en autograd.md, donde $u$ alimentaba a $f_2$ y a $f_3$ y su gradiente era la suma de ambas ramas. Acá el fan-out tiene $n_{l+1}$ ramas en vez de 2 (una por cada neurona de la capa siguiente), y el producto fila-por-matriz $\delta^{(l+1)}\cdot\Theta^{(l)}$ ya hace esa suma solo: la entrada $j$ del resultado es $\sum_i \delta_i^{(l+1)}\Theta_{ij}^{(l)}$, la suma de lo que aporta cada neurona de salida $i$ hacia la neurona de entrada $j$.

#### El gradiente que gradient descent realmente usa

$\delta^{(l)}$ es la Jacobiana respecto a las *activaciones*, pero lo que gradient descent actualiza son los *pesos* $\Theta_{ij}^{(l)}$. Como $z_i^{(l+1)}=\sum_j \Theta_{ij}^{(l)}a_j^{(l)}$, la derivada de $z_i^{(l+1)}$ respecto al peso $\Theta_{ij}^{(l)}$ es simplemente $a_j^{(l)}$ (todo lo demás de esa suma es constante respecto a ese peso). Entonces:

$$\frac{\partial J}{\partial \Theta_{ij}^{(l)}} = \underbrace{\Big(\delta_i^{(l+1)}\cdot g'(z_i^{(l+1)})\Big)}_{\text{cuánto le importa a } J \text{ el pre-activación } z_i^{(l+1)}}\cdot\ a_j^{(l)}$$

que es exactamente el gradiente que aparece en la actualización $\Theta^{(l)} := \Theta^{(l)} - \alpha \dfrac{\partial J}{\partial \Theta^{(l)}}$ de gradient descent.

#### El paralelo completo

| autograd.md | redes_neuronales.md |
|---|---|
| Nodo $u=f_1(x)$ con fan-out hacia $p=f_2(u)$ y $q=f_3(u)$ | Capa $a^{(l)}$ con fan-out hacia cada neurona de $z^{(l+1)}=\Theta^{(l)}a^{(l)}$ |
| Jacobianas locales $Df_2$, $Df_3$ | Jacobianas locales $\Theta^{(l)}$ (lineal) y $\text{diag}(g')$ (sigmoide elemento a elemento) |
| Backward: $\partial L/\partial u = \partial L/\partial p\cdot Df_2 + \partial L/\partial q\cdot Df_3$ | Backward: $\delta^{(l)}=\delta^{(l+1)}\cdot\text{diag}(g'(z^{(l+1)}))\cdot\Theta^{(l)}$ (la suma del fan-out ya viene empaquetada en el producto matricial) |
| Se evita expandir $L(x_1,x_2)$ completo (expression swell) | Se evita expandir $h_\Theta(x)$ completo — por eso backprop es mucho más barato que derivar la fórmula gigante a mano |

Backpropagation, entonces, no es un algoritmo especial inventado para redes neuronales: es la regla de la cadena de Jacobianas de autograd.md, aplicada al grafo específico que arma una red neuronal (capas lineales $\Theta^{(l)}$ intercaladas con capas de sigmoide elemento a elemento), recorrido de atrás hacia adelante para reusar cálculos, y sumando en cada nodo con fan-out.

### ¿Cuál es la frontera de decisión?

En logistic regression la frontera de decisión era una sola recta (o hiperplano): el lugar donde $\theta^T x = 0$, es decir, donde $g(z) = 0.5$.

En una red neuronal, **cada neurona de la capa oculta define su propia recta** en el espacio de entrada (su propio $z_i^{(2)} = 0$). La capa de salida no combina los datos originales $x$ directamente, sino que combina el resultado de esas rectas (ya filtradas por la sigmoide). Esto quiere decir que la frontera final es la combinación no lineal de varias rectas, lo cual permite formar regiones curvas, cerradas, o separadas en varios pedazos.

Un ejemplo clásico es XOR: los puntos $(0,0)$ y $(1,1)$ son de una clase, y $(0,1)$ y $(1,0)$ son de la otra. No existe ninguna recta que separe estos dos grupos, así que logistic regression **no puede resolverlo**. Pero con una capa oculta de 2 neuronas, cada una traza una recta distinta (por ejemplo, una separando $(0,0)$ del resto y otra separando $(1,1)$ del resto), y la capa de salida combina ambos resultados para formar una frontera en forma de "franja", que sí logra separar correctamente las dos clases.

> Entre más neuronas tenga la capa oculta, más rectas se combinan, y más compleja/curva puede ser la frontera de decisión final. Esa es la razón de fondo por la que las redes neuronales pueden aprender patrones que logistic regression, por sí sola, no puede.

### Resumen

| Concepto           | Logistic Regression                          | Redes Neuronales                                                                 |
|---------------------|-----------------------------------------------|------------------------------------------------------------------------------------|
| Hipótesis           | $h_\theta(x) = g(\theta^T x)$                 | $h_\Theta(x) = g(\Theta^{(L-1)} \cdots g(\Theta^{(2)} g(\Theta^{(1)} x)))$ (composición de regresiones logísticas) |
| Parámetros          | vector $\theta$                               | una matriz $\Theta^{(l)}$ por cada par de capas                                   |
| Función de costo    | log loss sobre 1 salida                       | log loss sumado sobre $K$ salidas, + regularización sobre todos los $\Theta^{(l)}$ |
| Frontera de decisión| una recta (hiperplano)                        | combinación no lineal de varias rectas → puede ser curva, cerrada o disjunta       |
| Optimización        | gradient descent con derivada directa         | gradient descent con backpropagation (producto de Jacobianas capa por capa, con suma en cada fan-out) |
