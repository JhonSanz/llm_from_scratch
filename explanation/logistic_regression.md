# Repaso de conceptos

Después de entender como funciona linear regression, vamos a rescatar algunos conceptos clave que nos serviran como punto de partida para logistic regression.

#### Ejemplos de entrenamiento

Los ejemplos de entrenamiento son vectores n dimensionales que representan caracteristicas con valores numericos. Al tener varios ejemplos de entrenamiento y varias características podemos acomodar todo en una matriz.

Por ejemplo en esta tabla hay datos de varias casas y cada casa tiene valores para cada caracteristica. Entonces cada fila es una casa, y cada colunma es una caracteristica de la casa

| size  | number of bedrooms | number of floors | age of home | price |
|-------|--------------------|------------------|-------------|-------|
| 2104  | 5                  | 1                | 45          | 460   |
| 1416  | 3                  | 2                | 40          | 232   |
| 1543  | 6                  | 4                | 20          | 2345  |
| 163   | 2                  | 2                | 22          | 123   |
| ↑     | ↑                  | ↑                | ↑           | ↑     |
| $x_1$ | $x_2$              | $x_3$            | $x_4$       | $y$   |

así pues

$$X = \begin{bmatrix}
x_1^{(1)} & x_2^{(1)} & x_3^{(1)} & x_4^{(1)} \\
x_1^{(2)} & x_2^{(2)} & x_3^{(2)} & x_4^{(2)} \\
x_1^{(3)} & x_2^{(3)} & x_3^{(3)} & x_4^{(3)} \\
x_1^{(4)} & x_2^{(4)} & x_3^{(4)} & x_4^{(4)}
\end{bmatrix}$$

osea

$$X = \begin{bmatrix}
2104 & 5 & 1 & 45 \\
1416 & 3 & 2 & 40 \\
1543 & 6 & 4 & 20 \\
163 & 2 & 2 & 22
\end{bmatrix}$$

Y se introducen estas notaciones para acceder a los diferentes vectores y valores

$$x^{(2)} = \begin{bmatrix}
1416 \\
3 \\
2 \\
40
\end{bmatrix} \quad x_3^{(2)} = 2$$


#### Variable salida / objetivo

Ahora analicemos la ultima columna, en este ejemplo es el precio de la casa. Esto es lo que queremos inferir para un nuevo ejemplo después de realizar el entrenamiento. Es también un vector, y aunque la nomenclatura sea un poco confusa, obtenemos los datos de la siguiente manera

$$y= \begin{bmatrix}
460 \\
232 \\
2345 \\
123
\end{bmatrix} \quad y^{(2)} = 232$$

#### Hipótesis

Ahora que tenemos los datos de entrenamiento, vamos a formular una hipótesis. Esta es una función que nos servirá para **describir** nuestros datos, por lo tanto, despendiendo de lo que querramos hacer la hipótesis va a ser diferente.

En la regresión lineal utilizabamos una recta, la cual "acomodabamos" para que se adaptara lo mejor posible a los datos. Entonces, la hipótesis era la recta

$$h_\theta(x) = \theta_0 + \theta_1 x$$

#### Parámetros

Como podemos observar, la recta depende de unos valores $\theta$ que definen la pendiente y posición de la recta. Estos son los parámetros que se optmizan durante la fase de entrenamiento y de esta manera el modelo "aprende".

$\theta_0$ es el punto de corte con el eje Y. 

$\theta_1$ es la pendiente de la recta.

Si consideramos que nuestros datos de entrenamiento tiene varias características, entonces $\theta$ es también un vector

$$\theta = \begin{bmatrix}
\theta_0 \\
\theta_1 \\
\theta_2 \\
\vdots \\
\theta_n
\end{bmatrix}$$

es decir, nuestra hipótesis sería una recta como esta

$$h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \dots + \theta_n x_n$$

donde vemos que aparecen ambas $X$ y $\theta$, y como sigue siendo una recta, el parámetro $\theta_0$ sigue siendo el desplazamiento de la recta, y esta no depende de $X$.

#### Sesgo

Así que, como nos gusta la elegancia y la facilidad vamos a hacer lo siguiente: Definamos de nuevo a X, y hagamos un producto de vectores


$$x = \begin{bmatrix}
x_0 \\
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{bmatrix} 
\quad 
\theta = \begin{bmatrix}
\theta_0 \\
\theta_1 \\
\theta_2 \\
\vdots \\
\theta_n \\
\end{bmatrix}$$

Como vimos al inicio las catacterísticas se definieron con $x_1, x_2, \dots, x_4, \dots, x_n$, pero... 👀 ahí no está $x_0$, es justo que agregamos recientemente. A partir de ahora siempre $x_0 = 1$. De esta manera podemos hacer esto

$$\theta^T \cdot X = \begin{bmatrix} \theta_0 & \theta_1 & \theta_2 & \dots & \theta_n \end{bmatrix}  \cdot
\begin{bmatrix}
x_0 = 1 \\
x_1 \\
x_2 \\
\vdots \\ 
x_n \\
\end{bmatrix} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n$$

Y esto se conoce como la forma vectorial de la hipótesis.

#### Función de costo

Ahora que tenemos todos los elementos para escribir matemáticamente nuestro problema, se introduce la función que sirve para **saber qué tan buenos son nuestros parámetros $\theta$**, es decir, necesitamos medir qué tan lejos están nuestras predicciones $h_\theta(x)$ de los valores reales $y$. Por lo tanto, podemos decir que el costo es un único valor, entre mas cerca a cero mejor son las predicciones.

Como vimos anteriormente para linear regression esta es la función de costo

$$J(\theta_0, \theta_1, \dots, \theta_n) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$$

Queríamos encontrar el error cuadratico medio, es decir, qué tan lejos estaba nuestra hipótesis (nuestra linea recta) de los puntos. Eso está mejor explicado en el tutorial anterior

#### Optimización

Ya tenemos todos los componentes, solo falta el algoritmo que hace mínimo el costo. Para que el costo sea mínimo los parámetros $\theta$ deben ajustarse. Dependiendo del problema el movimiento de los parámetros cumplira un objetivo diferente, si es regresión los parametros ajustarán la recta los datos, si es clasificación la recta separará mejor los datos.

Existen muchos algoritmos para optimizar, uno muy famoso es el gradient descent. Para esto está el otro tutorial

# Logistic Regression

Este es el problema que se plantea:

Tenemos un dataset y queremos responder a la pregunta **que tan probable** es que cada ejemplo pertenezca o no a una categoría

Por ejemplo **que tan probable es que**... el email es o no spam, el paciente tiene un tumor con cancer o no, aplica o no aplica al descuento etc.

Para generalizar, llamamos al si y no como categorías, porque mas adelante veremos que se puede clasificar en mas de dos categorías. Por ahora tenemos la categoría 1 y la categoría 0

Imaginemos primero un plano cartesiano con puntos, ignoresmos el resto de la información


![alt text](img/image.png)

Aqui vemos unos puntos rojos y unos puntos azules, nuestro objetivo es separarlos de la mejor manera posible. En la siguiente imagen podemos ver varios intentos de rectas para separar los datos

![alt text](img/image-1.png)

la pregunta es ¿cómo elegimos esa recta?, este ejemplo es sencillo, pero nuestro dataset podría ser mucho mas complejo, con puntos que se superponen unos con otros, como una nube de las categorias mezcladas.

Empecemos entonces a rescatar conocimiento que aprendimos de linear regression. Aprendimos que una recta puede ser nuestra hipótesis

$$h_\theta(x) = \theta_0 + \theta_1 x$$

Pero aquí no nos sirve, porque la recta por si sola no puede darnos la información de la clasificación. Es decir, no hay una manera clara en que esta ecuación nos diga si un ejemplo pertenece o no pertenece a una categoría. **Osea, esta ecuación no nos retorna un valor 0 o 1** sino que su rango es $-\infty$ hasta $+\infty$, y por tanto no responde a la pregunta de **qué tan probable es...** ya que la probabilidad se da entre 0 y 1

#### Decision boundary

Intuitivamente y visualmente podemos ver algo en lo que la recta es muy buena, sirve como límite para decir "aqui empieza una categoría y aqui termina la otra". Por eso se le llama decision boundary, porque es la frontera, el límite. Por lo cual conservaremos la recta para nuestro estudio

#### Sigmoid function

Entonces estamos en el dilema de elegir una hipótesis que nos diga **la probabilidad** de si un ejemplo de entrenamiento pertenece o no pertenece a una categoría. Y hay una función bella que nos ayuda a esto, es la sigmoid function:

$$g(z) = \frac{1}{1 + e^{-z}}$$

#### "Disección" analítica de la Sigmoid function

Antes de presentar esta función graficada pensemos un poco...

##### Dominio de la función:

Analizando el denominador encontramos que 

$$1+e^{-z} \neq 0 \forall z \in \mathbb{R}$$

ya que $e^{x}, x \in \mathbb{R}$ nunca es -1 ya que $ln(-1)$ no está definido


##### Rango de la función