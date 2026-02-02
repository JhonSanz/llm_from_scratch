# Aplicaciones a Geometría Analítica

Vamos a realizar el análisis de todo lo que aprendimos para definir algunas cuesitones geométricas. Vamos a definir cosas como recta, plano y "en". Todo esto aplica para $R_n$, sin embargo por temas de visualización vamos a utilizar $R_3$ y hacer unas gráficas bien sabrosas

Vamos a emplezar las operaciones algebráicas de suma y multiplicación por escalar en $V_n$

## La Recta

Sea $P$ un punto y un vector $A$ no nulo. El conjunto de todos los puntos de la forma $P + tA$ con $t \in  \mathbb{R}$, es **una recta** que pasa por $P$ y es paralela a $A$. Designaremos esa recta con $L(P; A)$ 

$$L(P; A) = \{ P + tA | t \in  \mathbb{R}\}$$

> Recordando... $L$ es el envolvente lineal. Es un conjunto de $n$ vectores los cuales se les hace la combinación lineal con n constantes. Entonces el envolvente lineal $L$ genera vectores

En este caso, los vectores generados por $L$ son los vectores que describen una linea recta, y veamos estos enunciados importantes

En $L(P; A)$

1. El punto $P$ está en la recta, ya que corresponde a $t=0$
2. El vector $A$ se llama vector de dirección de la recta
3. La recta $L(O; A)$ que pasa por el origen $O$ es el envolvente lineal de $A$, es decir todos los productos de $A$ por escalares. En este caso prácticamente el conjunto $S = \{ A \}$.
4. La recta $P$ paralela a $A$ se obtiene sumando $P$ a cada vector de la envolvente lineal de $A$

![alt text](img/rec_1.png)

[Ver en geogebra](https://www.geogebra.org/m/wnzeuzcw)

## Propiedades de las rectas

1. Podemos reemplazar el vector de dirección $A$ por uno paralelo a este. Es decir $A = cB$ o en otras palabras, $B$ es un múltiplo escalar de $A$ con $c \neq 0$. Por lo tanto, dos rectas $L(P;A)$ y $L(P;B)$ que pasan por el mismo punto son iguales si los vectores de dirección $A$ y $B$ son paralelos

2. Dos rectas $L(P;A)$ y $L(Q;A)$ con el mismo vector de dirección $A$ son iguales si $Q$ está en $L(P;A)$. Ya que, si $Q$ no está en $L(P;A)$, $L(Q;A)$ es una recta paralela pero no igual


![alt text](img/rec_2.png)

3. Dadas $L$ y un punto $Q \notin L$, existe solo una recta $L'$ que contiene $Q$ y es paralela a $L$. Como se ve en el gráfico, la única manera es que se elija el vector director paralelo a $L$, ya que por $Q$ pasan infinitas rectas diferentes

![alt text](image.png)

