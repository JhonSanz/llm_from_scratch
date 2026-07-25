En nuestra exploración de las funciones de varias variables comentamos bastantes aspectos efocándonos en los campos escalares; aquí vamos a ver tanto campos escalares como vectoriales y con particular atención la regla de la cadena en ambos casos

![regla_cadena_escalares](img/r_cadena_escalares.png)

> ver demostración Cálculo Tom M. Apostol vol 2 Pág 214

Ya hemos explorado bstante la teoría. Veamos un ejemplo muy bello

## Ejemplo donde vamos a aplicar muchas cosas

Tenemos un campo escalar y una función vectorial

$$f(x,y) = 1.4-0.16(x²+y²) \quad \quad r(t) = (tcos(3t), tsen(3t))$$

esto nos dibuja una cúpula y una espiral en el plano $xy$

![cupula_espiral](img/cupula_espiral.png)

para empezar podemos hacer varios analisis. Tal y como dice el teorema 8.8 podemos armarnos una función nueva $g(t)$ la cual representa la composción del campo escalar con la función vectorial, y todo esto es posible porque el resultado de la función vectorial corresponde con la entrada que el campo escalar espera

por lo tanto hacer

$$g(t) = f[r(t)]$$

hace que cuando el parámetro $t$ cambia estamos "surfeando" la cupula siguiendo la trayectoria de la espiral que está dibujada en el plano $xy$, y de ahí salen varios razonamientos, que de hecho el autor del libro comenta

![temperatura](img/temperatura.png)

Entonces imaginemos eso, estamos analizando la temperatura de esa cúpula a medida que bajamos siguiendo esa trayectoria con forma de espiral. Pongamos algunos valores de ese movimiento

| $t$ | $r(t)$ | $f[r(t)]$ |
|-----|--------|-----------|
||||||

Ahora bien, esto al mismo tiempo nos dice la temperatura en un punto dado de la superficie. Entonces volvemos al mismo análisis de siempre, como medimos la variación de la temperetura en un punto? ahí es donde aparece la derivada

Recientemente vimos el gradiente, veamos primero qué es lo que hace en la práctica


$$\frac{\delta f}{\delta x} = -0.32x \quad \frac{\delta f}{\delta y} = -0.32y$$

entonces tenemos

$$\nabla f = (-0.32x, -0.32y)$$

