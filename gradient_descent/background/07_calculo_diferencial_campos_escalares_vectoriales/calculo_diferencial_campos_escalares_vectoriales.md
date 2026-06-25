297-324

# CALCULO DIFERENCIAL EN CAMPOS ESCALARES Y VECTORIALES

En este punto ya conocemos bastantes cosas:

- Vimos funciones de $\mathbb{R}$ a $\mathbb{R^n}$ las cuales describian movimiento de particulas en el espacio y otros temas interesantes relacionados a vectores
- Vimos algo de la fundamentación de espacios lineales y transformaciones lineales

En este punto el autor nos propone tener transformaciones lineales $T: \mathbb{R^n} \to \mathbb{R^m}$ pero con la diferencia de que $T$ no sea lineal, apensar de que $V$ y $W$ si sean espacios lineales de dimensión finita

En particular cuando tenemos:

- Una función $T: \mathbb{R^n} \to \mathbb{R}$ le llamamos campo escalar
- Una función $T: \mathbb{R^n} \to \mathbb{R^m}$ le llamamos campo vectorial

El autor también propone utilizar el producto interior y norma así

$$x \cdot y = \sum_{k=1}^{n} x_{k} y_k$$

$$\lVert x \rVert = (x \cdot x)^{-1}$$

Investigando un poco y hablando con la IA me menciona lo siguiente

> Y aquí está la idea profunda: la linealidad no desaparece, se muda del nivel global al nivel local. Aunque $T$ globalmente sea curva, si haces zoom infinito alrededor de un punto $a$, la función se ve recta. Ese mapa lineal local que aproxima a $T$ cerca de $a$ es la derivada, $DT(a): \mathbb{R}^n \to \mathbb{R}^m$ y esa sí es una transformación lineal entre espacios vectoriales, representada por una matriz: la jacobiana. Toda la maquinaria de la Parte 1 reaparece, pero como modelo infinitesimal de la Parte 2.

Todo esto aparecerá en su momento, por ahora veamos lo fundamental de este tipo de funciones. Como vimos al inicio estas funciones se caracterizan por tener como argumento un vector de $ \mathbb{R^n}$ y eso tiene unas implicaciones importantes

## Bolas abiertas y conjuntos abiertos

Sean $a$ un punto dado en $\mathbf{R}^n$ y $r$ un número positivo dado. El conjunto de
todos los puntos $x$ de $\mathbf{R}^n$ tales que

$$\lVert x - a \rVert \lt r$$

se llama **$n$-bola abierta** de radio $r$ y centro $a$. Designamos este conjunto con $B(a; r)$.

recordando que la norma nos indica también la distancia al origen, por lo tanto si el centro de la bola es $a$ entonces si $x$ excede $r$ se considera que está fuera de ella

La bola $B(a; r)$ está constituida por los puntos cuya distancia a $a$ es menor
que $r$. En $\mathbf{R}^1$ es simplemente un intervalo abierto con punto medio en $a$. En $\mathbf{R}^2$
es un disco circular, y en $\mathbf{R}^3$ es un sólido esférico con centro en $a$ y radio $r$.

Esto es importante porque este tipo de funciones puede tener $n$ cantidad de coordenadas de entrada

**DEFINICIÓN DE PUNTO INTERIOR.** *Sea $S$ un subconjunto de $\mathbf{R}^n$, y supongamos que $a \in S$. Se dice que $a$ es punto interior de $S$ si existe una $n$-bola abierta con centro en $a$, cuyos puntos pertenecen todos a $S$.*

Es decir, todo punto $a$ interior de $S$ puede rodearse por una $n$-bola $B(a)$ tal
que $B(a) \subseteq S$. El conjunto de todos los puntos interiores de $S$ se llama el *interior*
de $S$ y se designa con $int S$. Un conjunto abierto que contenga un punto $a$ se llama
a veces *entorno* de $a$.

**DEFINICIÓN DE CONJUNTO ABIERTO.** *Un conjunto $S$ de $\mathbf{R}^n$ se llama abierto si todos sus puntos son interiores. Es decir, $S$ es abierto si y sólo si $S = int S$.*


graficamente podemos verlo así 

![bolas](img/bolas.png)