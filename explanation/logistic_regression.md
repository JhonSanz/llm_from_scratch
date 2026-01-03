# Logictic Regression

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
| $x_1$ | $x_2$              | $x_3$            | $x_4$       | $x_5$ |

así pues

$$X = \begin{bmatrix}
x_1^{(1)} & x_2^{(1)} & x_3^{(1)} & x_4^{(1)} & x_5^{(1)} \\
x_1^{(2)} & x_2^{(2)} & x_3^{(2)} & x_4^{(2)} & x_5^{(2)} \\
x_1^{(3)} & x_2^{(3)} & x_3^{(3)} & x_4^{(3)} & x_5^{(3)} \\
x_1^{(4)} & x_2^{(4)} & x_3^{(4)} & x_4^{(4)} & x_5^{(4)}
\end{bmatrix}$$

osea

$$X = \begin{bmatrix}
2104 & 5 & 1 & 45 & 460 \\
1416 & 3 & 2 & 40 & 232 \\
1543 & 6 & 4 & 20 & 2345 \\
163 & 2 & 2 & 22 & 123
\end{bmatrix}$$

Y se introducen estas notaciones para acceder a los diferentes vectores y valores

$$x^{(2)} = \begin{bmatrix}
1416 \\
3 \\
2 \\
40
\end{bmatrix} \quad x_3^{(2)} = 2$$

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

Como vimos al inicio las catacterísticas se definieron con $x_1, x_2, \dots, x_5, \dots, x_n$, pero... 👀 ahí no está $x_0$, es justo que agregamos recientemente. A partir de ahora siempre $x_0 = 1$. De esta manera podemos hacer esto

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

