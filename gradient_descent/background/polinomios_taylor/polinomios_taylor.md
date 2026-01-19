# Aproximación de funciones por medio de Polinomios de Taylor

Supongamos que tengo una función $f$ y una función desconocida que es muy parecida, es decir, la diferencia entre ambos resultados para un punto $a$ cualquiera es muy pequeña.

Ahora supongamos que esta función desconocida es un polinomio. Como la diferencia entre $f$  y nuestra funcion polinomio es muy pequeña, podríamos concluir que podría calcular directamente con el polinomio.

Esto sería muy conveniente ya que los polinomios son fáciles de calcular, se trata de sumas y multiplicaciones.

#### Ejemplo

Supongamos la función

$$f(x) = e^x$$

para $x = 0$ entonces $f(0) = 1$. Esto pasa para $f$ y todas sus derivadas

Ahora supongamos el polinomio de primer grado

$$g(x) = 1 + x$$

vemos que 

$$g(0) = 1 $$
$$g'(x) = 1  \rightarrow g'(0) = 1 $$

> Osea, $g$ coincide con $f$ y su primera derivada en $0$

Ahora probemos con otro polinomio desconocido $h$, pero esta vez uno de segundo grado, pero ahora que coincida con $f$ hasta la segunda derivada en 0, es decir:

$$h(0) = f(0) = 1$$
$$h'(0) = f'(0) = 1$$
$$h''(0) = f''(0) = 1$$

Si esto se cumple podríamos esperar una mejor aproximación de f, por lo menos en las proximidades de $(0, 1)$. Probemos con este

$$h(x) = 1 + x + \frac{1}{2}x^2 $$

vemos que cumple las condiciones anteriores.

$$h(0) = 1 + 0 + \frac{1}{2}0^2 = 1$$
$$h'(x) = 1 + x \rightarrow h'(0) = 1$$
$$h''(x) = 1 \rightarrow h''(0) = 1$$


#### Grafiquemos estas tres funciones

<!-- ![alt text](img/ex_1.png) -->

vemos como $h$ se empieza a parecer visualmente a $f$

# Encontrando el polinomio

> Cálculo de Tom Apostol Vol. 1 pag 335
>
>Supongamos que $f$ tiene derivadas hasta el orden $n$ el en punto $x = 0$, siendo $n \geq 1$, e intentemos encontrar un polinomio $P$ que coincida con $f$ y sus $n$ primeras derivadas en $0$, deben satisfacerse $n + 1$ condiciones, a saber
>
>$$P(0) = f(0)$$
>$$P'(0) = f'(0)$$
>$$\vdots$$
>$$P^{(n)}(0) = f^{(n)}(0)$$
>
>
>Así que ensayamos un polinomio de grado $n$, por ejemplo
>
>$$P(x) = c_0 + c_1x + c_2x^2 + \dots + c_nx^n$$
>
> con $n + 1$ coeficientes por determinar

Veamos el varios pasos sucesivos

$x = 0$

---


$P(0) = c_0 \rightarrow f(0) = c_0$

$\text{ya que } P(0) = c_0 + c_1x + c_2(0)^2 + c_3(0)^3 + c_4(0)^4 +  \cdots + c_nx^{n}$

$\text{osea } P(0) = c_0 \text{ y además } P(0) = f(0)$

$\text{entonces } f(0) = c_0$

---

$P'(0) = c_1 \rightarrow f'(0) = c_1 $

$\text{ya que } P'(0) = 0 + c_1 + 2c_2(0) + 3c_3(0)^2 + 4c_4(0)^3 +  \cdots + nc_n(0)^{n - 1}$

$\text{osea } P'(0) = c_1 \text{ y además } P'(0) = f'(0) $

$\text{entonces } f'(0) = c_1$

---

$P''(0) = 2c_2 $

$\text{ya que } P''(0) = 0 + 0 + 2c_2 + 6c_3(0) + 12c_4(0)^2 +  \cdots + nc_n(0)^{n - 1}$

$\text{osea } P''(0) = 2c_2 \text{ y además } P''(0) = f''(0)$

$\text{entonces } \frac{f''(0)}{2} = c_2$

---

$P'''(0) = 6c_3$

$\text{ya que } P'''(0) = 0 + 0 + 0 + 6c_3 + 24c_4(0) + \cdots + nc_n(0)^{n - 1}$

$\text{osea } P'''(0) = 6c_3 \text{ y además } P'''(0) = f'''(0) $

$\text{entonces } \frac{f'''(0)}{6} = c_3$

---

y en general $P^{(k)}(0) = k!c_k$

osea que podemos determinar las constantes así

> $$c_k = \frac{f^{(k)}(0)}{k!} $$

Este razonamiento demuestra que existe un polinomio de grado $\leq n$ que satisface las $n+1$ condiciones en el punto $x = 0$


$$P(0) = f(0)$$
$$P'(0) = f'(0)$$
$$\vdots$$
$$P^{(n)}(0) = f^{(n)}(0)$$

Este polinomio viene dado por 

> $$ P(x) = \sum_{k = 0}^{n} \frac{f^{k}(0)}{k!}x^k$$

Similarmente podemos demostrar que existe un polinomio de grado  $\leq n$ que coincide con $f$ y sus $n$ primeras derivadas en el punto $x = a$

Hagamos de nuevo un par de iteraciones, esta vez probando este polinomio

$$P(x) = c_0 + c_1(x - a) + c_2(x - a)^2 + c_3(x - a)^3 + \dots + c_n(x - a)^n$$

y estas condiciones

$$P(a) = f(a)$$
$$P'(a) = f'(a)$$
$$\vdots$$
$$P^{(n)}(a) = f^{(n)}(a)$$

Entonces

$x = a$

---


$P(a) = c_0 \rightarrow f(a) = c_0$

$\text{ya que } P(a) = c_0 + c_1\cancel{((a) - a)} + c_2\cancel{((a) - a)}^2 + c_3\cancel{((a) - a)}^3 + c_4\cancel{((a) - a)}^4 +  \cdots + c_n\cancel{((a) - a)}^{n}$

$\text{osea } P(a) = c_0 \text{ y además } P(a) = f(a)$

$\text{entonces } f(a) = c_0$

---

$P'(a) = c_1 \rightarrow f'(a) = c_1 $

$\text{ya que } P'(a) = 0 + c_1 + 2c_2\cancel{((a) - a)} + 3c_3\cancel{((a) - a)}^2 + 4c_4\cancel{((a) - a)}^3 +  \cdots + nc_n\cancel{((a) - a)}^{n - 1}$

$\text{osea } P'(a) = c_1 \text{ y además } P'(a) = f'(a) $

$\text{entonces } f'(a) = c_1$


Podemos seguir con el mismo razonamiento que antes y vamos a encontrar que 

> $$ P(x) = \sum_{k = 0}^{n} \frac{f^{k}(a)}{k!}(x - a)^k$$

Satisface las condiciones, y se llama Polinomio de Taylor de grado $n$ generado por $f$ en el punto $a$.


### Notación


Es conveniente tener una notación que indique la dependencia del polinomio de Taylor $P$ respecto de $f$ y $n$. Así que utilizaremos el símbolo $T_nf$, $T_nf(x)$ o $T_n(f(x))$ y se denomina operador de Taylor de grado $n$

Cuando el operador se aplica a una función $f$ genera una nueva función $T_nf$

El valor de esta función en $x$ se representa con $T_nf$, y con respecto de $a$ es $T_nf(x ; a)$


### Ahora el ejemplo de toda la vida (pero que es muy útil)

Encontremos el polinmio de taylor para la función $sen(x)$

$f(x) = sen(x) \rightarrow f(0) = 0$

$f'(x) = cos(x) \rightarrow f'(0) = 1$

$f''(x) = -sen(x) \rightarrow f''(0) = 0$

$f'''(x) = -cos(x) \rightarrow f'''(0) = -1$

$f^{4}(x) = sen(x) \rightarrow f^{4}(0) = 0$

$\vdots$

$etc$

entonces $f^{(2n + 1)}(0) = (-1)^n$ y a su vez $f^{(2n)}(0) = 0$


Osea solo aparecen potencias impares de $x$ en los polinomios de Taylor generados por la función $sen(x)$ en $x = 0$. Entonces

$$T_{2n + 1}(sen(x)) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots + (-1)^n \frac{x^{2n + 1}}{(2n + 1)!}$$


Si hacemos el mismo razonamiento para la función $cos(x)$ (de hecho funciona el razonamiento de arriba) vemos que los polinomios de taylor generados por la función $cos(x)$ en $x = 0$ solo contiene potencias pares de $x$. Entonces

$$T_{2n}(sen(x)) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots + (-1)^n \frac{x^{2n}}{(2n)!}$$


### Algunas curiosidades






