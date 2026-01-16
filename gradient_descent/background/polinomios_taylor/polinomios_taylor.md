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

![alt text](img/ex_1.png)

vemos como $h$ se empieza a parecer visualmente a $f$

# Encontrando el polinomio

