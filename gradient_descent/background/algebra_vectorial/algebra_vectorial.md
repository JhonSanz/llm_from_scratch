# Interpretación

Existen tres métodos escencialmente distintos para introducir el álgebra vectorial:

##### Geométricamente

Los vectores se representan por segmentos orientados o flechas. Las operacion es algebráicas con vectores como + - * por números reales se definen y estudian por métodos geométricos.

##### Analíticamente

Los vectores y las operaciones se expresan mediante números llamados componentes. Entonces, las propiedades se deducen a partir de las propiedades de los números de las componentes. La descripción analítica de los vectores surge espotáneamente de la representación geométrica en cuanto se introduce un sistema coordenado.

##### Axiomáticamente

No se intenta describir la naturaleza de un vector o de las operaciones algebráicas, en su lugar se imaginan como conceptos no definidos de los que nada se sabe excepto que satisfacen un cierto conjunto de axiomas.



Utilizaremos esos tres métodos simultaneamente en todo este análisis, ya que los tres son válidos al mismo tiempo. Lo importante es la comodidad y la facilidad, en algunas ocasiones las cosas se entenderán mejor con uno y no con los otros, pero eso lo veremos mas adelante....

La historia es que al inicio de todo, los griegos conocían como situar un punto en una recta, algo así como decir 1 está en el eje X. Mas adelante descartes introdujo el plano, y se dio cuenta de que podía ubicar un par de numeros $(a,b)$ allí, y también una terna $(a,b,c)$ en el espacio y así infinitamente sin limitaciones.

Entonces aquí tenemos nuestra primera idea, podemos considerar una n-pla $(a_1, a_2, \dots, a_n)$ como un punto n-dimensional. Dependiendo de la cantidad de componentes es el lugar donde vive, por ejemplo si nuestro punto n-dimensional es:

- $x = (a_1, a_2)$ entonces este es un punto del plano, o mejor dicho de $\reals^2$
- $x = (a_1, a_2, a_3)$ entonces este es un punto del espacio, o mejor dicho de $\reals^3$
- etc

"El conjunto de todos los vectores n-dimensionales se llama espacio vectorial de n-plas o n-espacio, designado con $V_n$. Para convertir $V_n$ en una estructura algebráica introducimos la igualda y adición de vectores y la multiplicación por escalar" - De hecho este enunciado es un análisis axiomático, que se puede explicar con los Espacios Lineales, un tema que veremos mas a profundidad en el futuro.

Por ahora, vale la pena enunciar los axiomas para $V_n$. Sean $A = (a_1, a_2, \dots, a_n)$ y $B = (b_1, b_2, \dots, b_n)$ de $V_n$, entonces:

- $A = B$ si $a_1 = b_1, a_2 = b_2 \dots a_n = b_n$
- $A + B = (a_1 + b_1, a_2 + b_2, \dots, a_n + b_n)$
- $cA = (ca_1, ca_2, \dots, ca_n)$ con $c \in \reals$
- $A + B = B + A$
- $A + (B + C) = (A + B) + C$
- $c(dA) = (cd)A$
- $O = (0,0, \dots, 0)$ y $A + O = A$
- $(-1)A = -A$

Hasta aqui hay una semejanza indistinguible entre un número complejo y un vector de dos dimensiones, ambos se diferencian al introducir el producto.

## Interpretación geométrica en $\reals^2$



![alt text](img/vec_1.png)
