# Cálculo con funciones vectoriales

Como vimos anteriormente, podríamos escribir una recta como $x(t) = P + tA$, donde $t \in \mathbb{R}$ se llama parámetro y su recorrido es la recta. A su vez, se llama función vectorial de variable real, ya que

$$f: \mathbb{R} \to \mathbb{R}^n$$

es decir, la función transforma el escalar $t$ en un vector n-dimensional.

### Operaciones algebráicas

Las operaciones usadas de álgebra vectorial pueden aplicarse para combinar dos funciones vectoriales o una vectorial con una función real, veamos:

Sean $F$ y $G$ dos funciones vectoriales y $u$ una función real (es decir una funcion de $\mathbb{R} \to \mathbb{R}$)

- $(F + G)(t) = F(t) + G(t)$

- $(uF)(t) = u(t)F(t)$

- $(F \cdot G)(t) = F(t) \cdot G(t)$

Si $F(t)$ y $G(t) \in \mathbb{R}^3$ 

- $(F \times G)(t) = F(t) \times G(t)$

Todo esto quiere decir que podemos operar entre funciones antes de evaluarlas y el resultado va a ser equivalente, ya que estas operaciones se definen punto a punto. Y todo esto es válido porque ya tenemos todo definido para el álgebra vectorial, y en escencia las funciones vectoriales nos dan como resultado vectores, entonces podemos naturalmente heredar las propiedades. 

Es mas, al principio todo lo habíamos expresado como conjuntos. La idea de introducir las funciones es de alguna manera conveniencia y otra capa de abstracción, pero en el fondo, las imágenes de estas funciones son vectores.

### Composición de funciones

En este caso es importante resaltar que solo podemos componer funciones vectoriales con funciones reales, ya que, como vimos anteriormente el parámetro para las funciones vectoriales es un número real, y eso es precisamente lo que nos retornan las funciones reales. Por lo cual:

$$G(t) = f(u(t)) \forall t \in D_u$$

$D_u$ es el dominio de la función $u$.

### Componentes

Si una función $F$ tiene sus valores en $V_n$ cada vector $f(t)$ tiene $n$ componentes y podemos escribir

$$F(t) = (f_1(t), f_2(t), \dots, f_n(t))$$

Es decir, cada función vectorial $F$ origina $n$ funciones reales $f_1, f_2, \dots, f_n$ cuyos valores en $t$ son los componentes de $f(t)$ 


### Limites

Me ha resultado mas dificil verlo, pero la intuición aqui es entender que estas funciones describen movimiento. Si imaginamos el parámetro t moviéndose, tenemos que imaginarnos al mismo tiempo el vector resultante moviéndose

![alt text](img/fvec_1.png)

[Ver en geogebra](https://www.geogebra.org/m/c54ep68m)

Por lo tanto, siguiendo la intuición podemos movernos a la izquierda y la derecha de $t$, porque sabemos que $t$ es un número real. 

La pregunta es, ¿cómo se entiende el límite? en el ejemplo de la imagen tenemos la función vectorial

$$f(t) = (t, t^2)$$

que dibuja una bella parábola. Vemos que a medida que movemos el parámetro $t$ se empieza a dibujar la parábola de izquierda a derecha, y si dijeramos algo como "Calculemos el límite cuando $t$ tiende a 2" por ejemplo, al mismo tiempo estamos diciendo que el vector que dibuja la parábola **tiende también a algún vector** que también está siendo dibujado a medida que se mueve $t$, en este caso

$$\lim_{t \to 2}{f(t)} = (2,4)$$

Entonces la idea es que calculamos el límite en cada componente porque de esa manera sabemos si el vector tiende a otro vector límite, y así podemos afirmar que **el límite de cada componente del vector debe existir** para que el límite exista

En conclusión estamos moviendo el parámetro de la función y ver que pasa con el vector resultante. ¿Éste se acerca a otro vector? ¿el vector da un salto y el límite no existe? etc. Por lo tanto

$$\lim_{t \to p}{f(t)} = (\lim_{t \to p}{f_1(t)}, \dots, \lim_{t \to p}{f_n(t)})$$

¿Qué pasa si el límite de una de las componentes del vector no existe?, en ese caso algo pasa con la curva que describe la función y entran conceptos como continuidad etc.

### Continuidad

Como vimos en las funciones $f: \mathbb{R} \to \mathbb{R}$ pensabamos en la continuidad como dibujar la gráfica sin levantar la mano. Aquí aplica lo mismo, y podemos usar esta función para ejemplificar

$$f(t) = (t, \frac{1}{|t|})$$

![alt text](img/fvec_2.png)


si calculamos el límite por izquierda y por derecha

$$\lim_{t \to 0^-}{f(t)} = (-0, \infty)$$

$$\lim_{t \to 0^+}{f(t)} = (0, \infty)$$

La segunda componente diverge en ambos casos, por lo tanto el límite no existe

> Recordemos que en el contexto de límites $t$ **no es cero** sino que **tiende a cero**. Y también, que $\infty$ no es un número, sino un concepto

En este ejemplo vemos que los vectores resultantes en el límite son imposibles y el límite no existe. En resumen, se debe cumplir


$$\lim_{t \to a}{f(t)} = f(a)$$

El límite debe existir, la función en ese punto debe existir y ambos resultados tienen que coincidir. En ese caso decimos que es continua

### Derivada

Similarmente, como vimos en el caso de funciones reales la derivada se define igual para funciones vectoriales. Devido al parámetro $t \in \mathbb{R}$ podemos pensar la derivada como la recta que pasa sobre la curva entre los puntos $f(x+h) - f(x)$, lo que pasa es que en este caso son vectores, pero podemos tratarlos indistintamente en este contexto

Hay un video muy bueno donde se explica la idea detrás de la derivada y como ese límite dibuja una recta tangente en las funciones reales https://www.youtube.com/watch?v=_6-zwdrqD3U

Como estamos en funciones vectoriales, la derivada surge del límite de los vectores secantes, y ese límite define el vector director de la recta tangente

$$f'(t) = \lim_{h \to 0}{\frac{f(t+h) - f(t)}{h}}$$


Recordemos algo útil y es la diferencia de vectores, y la ley del paralelogramo, en la imagen puede verse como al acercar estos dos vectores, la diferencia $f(x+h) - f(x)$ se acerca a un único punto. La división entre 
$h$ es necesaria porque la derivada no mide desplazamiento, sino cambio por unidad de parámetro.

![alt text](img/fvec_4.png)

[Ver en Geogebra](https://www.geogebra.org/m/hw8hn4g9)

> Lo importante es que ese vector no es la derivada, solo dice "cuánto me moví" al variar $h$

De igual manera, operamos entre componentes porque seguimos con la idea de "el vector tiene un poquito de derivada en $x$ y otro poco en $y$", entonces a medida que la separación $h$ entre los vectores de ese límite se acercan aparecerá el vector director de la recta tangente. 

De igual manera, el parámetro $h$ nos sirve para escalar el vector. Esto es muy importante, y sobre todo el hecho de 

De hecho, la recta aparece cuando utilizamos lo que aprendimos antes de las rectas. Ejemplo:

sea r la función vectorial $r(t) = (t, t^2, sen(t))$ en $p = \frac{\pi}{2}$

su derivada es $r'(t) = (1, 2t, cos(t))$

entonces podemos escribir la recta tangente así

$L(s) = r(p) + s \cdot r'(p)$

$L(s) = (\frac{\pi}{2}, \frac{\pi^2}{4}, 1) + s(1, \pi, 0)$

La derivada de una función vectorial en un punto es un vector tangente a la curva en ese punto. Dicho vector surge como el límite del cociente incremental y permite construir la recta tangente mediante la ecuación $L(s) = r(p) + s \cdot r'(p)$

![alt text](img/fvec_3.png)