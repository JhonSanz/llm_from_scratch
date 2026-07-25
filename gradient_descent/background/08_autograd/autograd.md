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

| $t$   | $r(t)$              | $f[r(t)]$ |
|-------|---------------------|-----------|
| $0$   | $(0,\ 0)$           | $1.40$    |
| $0.5$ | $(0.035,\ 0.499)$   | $1.36$    |
| $1$   | $(-0.990,\ 0.141)$  | $1.24$    |
| $1.5$ | $(-0.316,\ -1.466)$ | $1.04$    |
| $2$   | $(1.920,\ -0.559)$  | $0.76$    |


Ahora bien, esto al mismo tiempo nos dice la temperatura en un punto dado de la superficie. Entonces volvemos al mismo análisis de siempre, como medimos la variación de la temperetura en un punto? ahí es donde aparece la derivada

Recientemente vimos el gradiente, veamos primero qué es lo que hace en la práctica


$$\frac{\delta f}{\delta x} = -0.32x \quad \frac{\delta f}{\delta y} = -0.32y$$

$$\nabla f = (-0.32x, -0.32y)$$

Tomemos $(x,y) = (1,1)$

$$\nabla f(1,1) = (-0.32\cdot 1,\ -0.32\cdot 1) = (-0.32,\ -0.32)$$

la altura de la cúpula ahí es

$$f(1,1) = 1.4 - 0.16(1^2+1^2) = 1.08$$

Qué significa esto en la cúpula de temperatura:

- Estás parado en el punto $(1,1)$ de la superficie, donde la temperatura es $1.08$
- El vector $(-0.32,-0.32)$ vive en el plano $xy$ (no en 3D) y nos dice: si caminamos en esa dirección, la temperatura sube lo más rápido posible. Como $x=y=1$ y el vector apunta hacia $(-1,-1)$, tiene sentido: la cúpula es más caliente en el centro $(0,0)$, así que "subir" en temperatura es caminar hacia el centro
![gradiente_cupula](img/gradiente_cupula.png)
- La magnitud $|\nabla f(1,1)| = \sqrt{0.32^2+0.32^2} \approx 0.4525$ es la tasa máxima de cambio (por unidad de distancia) que se siente parado ahí
- Si camináramos en la dirección opuesta $(1,1)$ (alejándonos del centro), la temperatura bajaría a esa misma tasa
- Si camináramos perpendicular al gradiente, por ejemplo en dirección $(1,-1)$, la temperatura no cambiaría instantáneamente, nos moveríamos sobre una curva de nivel

Entonces para recapitular, tomamos un punto arbitrario $(1,1)$ e hicimos el análisis. Que pasa entonces con la composición? retomemos el ejemplo original con algunos valores

$$f(x,y) = 1.4-0.16(x²+y²) \quad \quad r(t) = (tcos(3t), tsen(3t))$$

$$\nabla f = (-0.32x, -0.32y)$$

tomemos un punto arbitrario **sobre la espiral**

$a = r(\frac{\pi}{3}) = (-\frac{\pi}{3}, 0)$

$\nabla f(a) = (-0.335103, 0)$


![gradiente_composicion](img/gradiente_composicion.png)

osea, pudimos componer $f$ con $r$ y cuando una particula se mueve sobre $r$ podemos calcular el gradiente sobre esa trayectoria y en cada punto obtenemos la dirección de mayor crecimiento

finalmente apliquemos la regla de la cadena, porque queremos obtener la variación de temperatura en el tiempo $t$, o que tan rapido cambia la temperatura en $t$

