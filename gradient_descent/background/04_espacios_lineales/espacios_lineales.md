# Espacios lineales

Recordando algunos de los conceptos que tratamos en el capítulo de álgebra vectorial, teníamos varias forma de intepretarlos: Algebráicamente, geométricamente y axiomáticamente

En este capítulo nos concetrarémos en analizar elementos matemáticos axiomáticamente, es decir, no intentaremos ahondar en la "forma" ni las como se realizan operaciones entre estos elementos, sino que exigimos que las operaciones cumplan ciertas propiedades que tomamos como axiomas

Según la RAE:
> #### Axioma
>
> - Proposición tan clara y evidente que se admite sin demostración.
> - Cada uno de los principios indemostrables sobre los que, por medio de un razonamiento deductivo, se construye una teoría.

ok, entonces para redondear esto. Los axiomas son la receta **para las operaciones** que se pueden realizar sobre unos elementos cualquiera

### Definición de espacio lineal

"Sea $V$ un conjunto no vacío de objetos llamados *elementos*. El conjunto $V$ se llama espacio lineal si satisface los diez axiomas siguientes:"

#### Axiomas de clausura

1. **CLAUSURA RESPECTO DE LA ADICIÓN** A todo par de elementos $x$ y $y$ de $V$ corresponde un elemento **único** de $V$ llamado la suma $x$ y $y$, designado por $x + y$.

2. **CLAUSURA RESPECTO DE LA MULTIPLICACIÓN POR NÚMEROS REALES**. A todo $x$ de $V$ y todo número real $a$ corresponde un elemento de $V$ llamado producto de $a$ por $x$, designado por $ax$.

#### Axiomas para la adición

3. **LEY CONMUTATIVA** Para todo $x$ y todo $y$ de $V$, tenemos $x + y$ = $y + x$

4. **LEY ASOCIATIVA** Cualesquiera que sean $x$, $y$, $z$ de $V$, tenemos $(x + y) + z = x + (y + z)$.

5. **EXISTENCIA DE ELEMENTO CERO** Existe un elemento en $V$, designado con el símbolo $O$, tal que $x + O = x$ para todo $x$ de $V$.

6. **EXISTENCIA DE OPUESTOS** Para todo $x$ de $V$, el elemento $(-1)x$
tiene la propiedad $x + (-1)x = O$

#### Axiomas para la multiplicación por números

7. **LEY ASOCIATIVA** Para todo $x$ de $V$ y todo par de números reales $a$ y $b$, tenemos $a(bx) = (ab)x$

8. **LEY DISTRIBUTIVA PARA LA ADICIÓN EN $V$**. Para todo $x$ y todo
$y$ de $V$ y todo número real $a$, tenemos $a(x +y) = ax + ay$

9. **LEY DISTRIBUTIVA PARA LA ADICIÓN DE NÚMEROS** Para todo $x$ de $V$ y todo par de números reales $a$ y $b$, tenemos $(a + b)x = ax + bx$

10. **EXISTENCIA DE ELEMENTO IDÉNTICO** Para todo $x$ de $V$, tenemos $1x = x$.

Cálculo de Tom Apostol Vol 2 Pág 4.

El texto nos recalca que los axiomas funcionan indistintamente para escalares reales o complejos, y dependiendo los que usemos el espacio lineal toma el nombre (espacio lineal real/complejo). A veces también se puede llamar espacio vectorial lineal o espacio vectorial nada mas.


##### Algunos ejemplos que me gustaron

Sea $V = V_n$, el espacio vectorial de todas las n-plas de números reales, con la adición y la multiplicación por escalares definidas en la forma ordinaria en función de los componentes.

Primero dejemos claro el escenario: estamos en $V_n$, el conjunto de todas las n-plas de números reales, con las operaciones:

$$x + y = (x_1 + y_1, \, x_2 + y_2, \, \ldots, \, x_n + y_n)$$
$$ax = (ax_1, \, ax_2, \, \ldots, \, ax_n)$$

donde $x = (x_1, \ldots, x_n)$, $y = (y_1, \ldots, y_n)$ y $a \in \mathbb{R}$.

###### Axioma 1 — Clausura respecto de la adición

Dados $x, y \in V_n$, su suma es $(x_1 + y_1, \ldots, x_n + y_n)$. Como cada $x_i, y_i \in \mathbb{R}$ y los reales son cerrados bajo la suma, cada componente $x_i + y_i \in \mathbb{R}$, por lo tanto $x + y \in V_n$. La unicidad viene de que la suma de reales es única.

###### Axioma 2 — Clausura respecto de la multiplicación por escalar

Dado $x \in V_n$ y $a \in \mathbb{R}$, el producto es $(ax_1, \ldots, ax_n)$. Como cada $ax_i \in \mathbb{R}$, el resultado pertenece a $V_n$.

###### Axioma 3 — Ley conmutativa

$$x + y = (x_i + y_i) = (y_i + x_i) = y + x$$

donde usamos que la suma de números reales es conmutativa componente a componente.

###### Axioma 4 — Ley asociativa de la adición

$$(x + y) + z = ((x_i + y_i) + z_i) = (x_i + (y_i + z_i)) = x + (y + z)$$

usando asociatividad de $\mathbb{R}$ en cada componente.

###### Axioma 5 — Existencia del elemento cero

El elemento cero es $O = (0, 0, \ldots, 0)$. Entonces:

$$x + O = (x_i + 0) = (x_i) = x$$

###### Axioma 6 — Existencia de opuestos

Para cada $x \in V_n$, tomamos $(-1)x = (-x_1, \ldots, -x_n)$. Entonces:

$$x + (-1)x = (x_i + (-x_i)) = (0, \ldots, 0) = O$$

###### Axioma 7 — Ley asociativa de la multiplicación por escalares

$$a(bx) = a(bx_i) = (abx_i) = (ab)x$$

usando asociatividad de la multiplicación en $\mathbb{R}$.

###### Axioma 8 — Ley distributiva respecto de la adición en $V$

$$a(x + y) = a(x_i + y_i) = (ax_i + ay_i) = ax + ay$$

usando distributividad en $\mathbb{R}$.

###### Axioma 9 — Ley distributiva respecto de la adición de escalares

$$(a + b)x = ((a+b)x_i) = (ax_i + bx_i) = ax + bx$$

###### Axioma 10 — Existencia del elemento idéntico

$$1 \cdot x = (1 \cdot x_i) = (x_i) = x$$

La idea central de todas estas demostraciones es la misma: como las operaciones en $V_n$ se definen componente a componente, heredamos directamente las propiedades del cuerpo $\mathbb{R}$. Entonces, ¿cómo se demuestran los axiomas de $\mathbb{R}$?, bueno... ese es un dilema, simplemente aceptamos que son verdaderos y los usamos para demostrar en otros contextos. No todo se puede demostrar

ahora, el texto propone el siguiente ejercicio

Sea $V$ el conjunto de todos los vectores $V_n$ ortogonales a un
vector no nulo dado $N$. Si $n = 2$, este espacio lineal es una recta que pasa por $O$ con $N$ como vector normal. Si $n = 3$, es un plano que pasa por $O$ con $N$ como vector normal.

Aqui estamos hablando también de $V_n$ como en el caso anterior, por lo tanto no es necesario demostrar todos los axiomas porque las propiedades se heredan y solo es necesario verificar unos axiomas en específico

### Subespacio