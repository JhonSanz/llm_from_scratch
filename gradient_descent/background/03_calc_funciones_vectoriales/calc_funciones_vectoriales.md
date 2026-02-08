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

que dibuja una bella parábola. Vemos que a medida que movemos el parámetro $t$ se empieza a dibujar la parábola de derecha a izquierda, y si dijeramos algo como "Calculemos el límite cuando $t$ tiende a 2" por ejemplo, al mismo tiempo estamos diciendo que el vector que dibuja la parábola **tiende también a algún vector** que también está siendo dibujado a medida que se mueve $t$, en este caso

$$\lim_{t \to 2}{f(t)} = (2,4)$$

Entonces la idea es que calculamos el límite en cada componente porque de esa manera sabemos si el vector tiende a otro vector límite, y así podemos afirmar que **el límite de cada componente del vector debe existir** para que el límite exista

En conclusión estamos moviendo el parámetro de la función y ver que pasa con el vector resultante. ¿Éste se acerca a otro vector? ¿el vector da un salto y el límite no existe? etc. Por lo tanto

$$\lim_{t \to p}{f(t)} = (\lim_{t \to p}{f_1(t)}, \dots, \lim_{t \to p}{f_n(t)})$$

¿Qué pasa si el límite de una de las componentes del vector no existe?, en ese caso algo pasa con la curva que describe la función y entran conceptos como continuidad etc.

### Continuidad

Como vimos en las funciones $f: \mathbb{R} \to \mathbb{R}$ pensabamos en la continuidad como dibujar la gráfica sin levantar la mano y sin dibujar picos. Aquí aplica lo mismo, y podemos usar el ejemplo clásico del valor absoluto, pero escrito como función vectorial

![alt text](img/fvec_2.png)

si calculamos el límite por izquierda y por derecha

$$\lim_{t \to 0^-}{f(t)} = (-0.000001, 0.000001)$$

$$\lim_{t \to 0^+}{f(t)} = (0.000001, 0.000001)$$

> Recordemos que en el contexto de límites $t$ **no es cero!** sino que **tiende a cero**

Y debido a esto vemos que el vector resultante al evaluar el límite es diferente por izquierda y por derecha, por lo tanto el límite no existe.
