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

<iframe 
  src="https://www.geogebra.org/m/wnzeuzcw"
  width="800"
  height="500"
  style="border:0;">
</iframe>