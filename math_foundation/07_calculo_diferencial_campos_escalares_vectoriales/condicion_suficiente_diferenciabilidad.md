# Condición suficiente de diferenciabilidad (Teorema 8.7)

*Apostol, Cálculo Vol. 2, §8.13*

Este documento remata la cadena del capítulo: vimos que ni las parciales ni las direccionales por sí solas sirven como "derivada" en varias variables, y que la buena definición es la **aproximación lineal con error $o(\|\mathbf{v}\|)$** (el $T_{\mathbf{a}}$). El problema es que esa definición es un cuantificador existencial incómodo de verificar a mano. El Teorema 8.7 da el **atajo práctico**.

## Primero lo importante: el 8.7 NO reemplaza a Taylor

Antes de entrar al teorema, hay que deshacer una confusión muy común: parece que aparecen **dos cosas distintas** compitiendo —el plano tangente de Taylor por un lado, y "las parciales continuas" por otro—. **No compiten. Son el mismo objeto visto desde dos preguntas.**

Hay dos personajes y conviene nombrarlos:

- **El plano tangente / Taylor de grado 1 — el QUÉ.** Es el objeto que quieres, tu intuición del "zoom": al acercarte a $\mathbf{a}$, la superficie se ve plana, y ese plano es

  $$f(\mathbf{a}+\mathbf{v}) \approx \underbrace{f(\mathbf{a})}_{\text{altura}} + \underbrace{\nabla f(\mathbf{a})\cdot\mathbf{v}}_{\text{inclinación} \,=\, T_{\mathbf{a}}(\mathbf{v})}$$

  Ser diferenciable es que este plano aproxime con error $o(\|\mathbf{v}\|)$. **Este plano es el protagonista.**

- **El Teorema 8.7 — el CÓMO LO VERIFICO.** No es otro plano. Es el **portero**: la condición fácil de chequear que te certifica que *ese mismo* plano de Taylor cumple la promesa del error. Vive **encima** de Taylor, garantizándolo, no en su lugar.

La clave que amarra todo: cuando el Teorema 8.7 termina su demostración, la parte lineal que obtiene es

$$\sum_{k=1}^n D_k f(\mathbf{a})\,v_k \;=\; \nabla f(\mathbf{a})\cdot\mathbf{v} \;=\; T_{\mathbf{a}}(\mathbf{v}),$$

es decir, **exactamente el plano tangente de Taylor**. El teorema no inventa un objeto aparte: construye ese mismo plano y prueba que el error que sobra es despreciable.

Por eso el gradiente aparece en los dos personajes (y por eso se confunden):

| | Papel del gradiente $\nabla f(\mathbf{a})$ |
|---|---|
| En Taylor / plano tangente | son los **coeficientes** del plano (la inclinación) |
| En la hipótesis del Teorema 8.7 | se pide que **las componentes de ese mismo gradiente** ($D_1 f,\dots,D_n f$) sean **funciones continuas** |

Es el mismo gradiente: Taylor lo usa para **armar** el plano; el 8.7 pide que ese gradiente sea continuo para **garantizar** que el plano sirve.

El orden lógico completo:

```
Taylor grado 1   →  define el plano tangente candidato:  f(a) + ∇f(a)·v
                    (tu intuición del zoom)
       ↓
Definición de    →  f es diferenciable SI ese plano aproxima
diferenciable        con error o(‖v‖)  (la promesa asintótica)
       ↓
Problema         →  verificar "error o(‖v‖) en todas las direcciones"
                    a mano es incómodo
       ↓
Teorema 8.7      →  atajo: si las parciales (= componentes del gradiente)
                    son continuas, la promesa se cumple sola. Y su
                    demostración ES el cálculo del error de ESE mismo
                    plano de Taylor.
```

Con eso claro, ahora sí el teorema.

## Las dos direcciones lógicas (no confundirlas)

El teorema convive con su recíproco falso. Grabar esto es media batalla:

- **Diferenciable $\Rightarrow$ existen las parciales.** (Teorema 8.5.) Pero **el recíproco es falso**: el contraejemplo $f(x,y)=\dfrac{xy^2}{x^2+y^4}$ tiene $D_1 f(\mathbf{O})$ y $D_2 f(\mathbf{O})$ y *no* es diferenciable (ni continua). **Tener parciales no basta.**
- **Parciales continuas $\Rightarrow$ diferenciable.** (Teorema 8.7.) Pero **el recíproco también es falso**: hay funciones diferenciables con parciales discontinuas. La condición es **suficiente, no necesaria**.

> **TEOREMA 8.7 (condición suficiente de diferenciabilidad).** Si existen las derivadas parciales $D_1 f, \dots, D_n f$ en una cierta $n$-bola $B(\mathbf{a})$ y son continuas en $\mathbf{a}$, entonces $f$ es diferenciable en $\mathbf{a}$.

## El nudo conceptual: ¿por qué "continuas" lo cambia todo?

La pregunta que confunde a todos: *¿por qué una condición sobre las parciales —que son solo $n$ direcciones, los ejes— alcanza a garantizar el buen comportamiento en TODAS las direcciones?*

La respuesta es la palabra **continuas**. Distingue dos niveles de información:

| | Qué te dice | Alcance |
|---|---|---|
| Parcial **existe en $\mathbf{a}$** | la pendiente sobre el eje, en **ese punto exacto** | puntual, $n$ direcciones, ciego a los vecinos |
| Parcial **continua en $\mathbf{a}$** | las pendientes de los puntos **vecinos** se parecen a la de $\mathbf{a}$ | **toda una vecindad** |

El salto: **"continua" convierte información de los ejes en información de toda la vecindad.** Y una vez que controlas la vecindad, controlas cualquier dirección $\mathbf{v}$, porque un desplazamiento arbitrario se descompone en una **escalera** de pasitos a lo largo de los ejes (la suma telescópica de la demostración), y en cada peldaño usas una parcial evaluada en un punto **intermedio** cercano a $\mathbf{a}$.

## La demostración de Apostol, paso a paso (§8.13, pp. 319-320)

Esta es la demostración **tal como está en el libro**. El eslabón es el [Teorema del valor medio para campos escalares](calculo_diferencial_campos_escalares_vectoriales.md) (8.4) — mejor dicho, su versión unidimensional aplicada peldaño a peldaño —: es lo único que traduce el incremento en parciales evaluadas en puntos intermedios.

**Preparación.** Escribimos $\lambda = \|\mathbf{v}\|$ y $\mathbf{v} = \lambda\mathbf{u}$ con $\|\mathbf{u}\|=1$, tomando $\lambda$ tan pequeño que $\mathbf{a}+\mathbf{v}$ esté en la bola $B(\mathbf{a})$ donde existen las parciales. Descomponemos el unitario en sus componentes $\mathbf{u} = u_1\mathbf{e}_1 + \dots + u_n\mathbf{e}_n$.

**Paso 1 — Suma telescópica escalonada (8.13).** El truco central: en vez de ir de $\mathbf{a}$ a $\mathbf{a}+\mathbf{v}$ en diagonal, vamos por una **escalera**, moviendo *una coordenada a la vez*. Definimos los vértices de la escalera

$$\mathbf{v}_0=\mathbf{0},\quad \mathbf{v}_1=u_1\mathbf{e}_1,\quad \mathbf{v}_2=u_1\mathbf{e}_1+u_2\mathbf{e}_2,\quad\dots,\quad \mathbf{v}_n=\mathbf{u},$$

de modo que $\mathbf{v}_k = \mathbf{v}_{k-1} + u_k\mathbf{e}_k$. Entonces el incremento total se telescopia:

$$f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) = \sum_{k=1}^n \big\{ f(\mathbf{a}+\lambda\mathbf{v}_k) - f(\mathbf{a}+\lambda\mathbf{v}_{k-1}) \big\}.$$

Cada término es un **peldaño**. Llamando $\mathbf{b}_k = \mathbf{a}+\lambda\mathbf{v}_{k-1}$, el $k$-ésimo peldaño es $f(\mathbf{b}_k + \lambda u_k\mathbf{e}_k) - f(\mathbf{b}_k)$: dos puntos que difieren **solo en la $k$-ésima coordenada**.

**Paso 2 — Valor medio en cada peldaño (8.14).** Justo porque los dos extremos del peldaño difieren en una sola coordenada, es un problema *unidimensional*, y aplica el valor medio del cálculo de una variable:

$$f(\mathbf{b}_k + \lambda u_k\mathbf{e}_k) - f(\mathbf{b}_k) = \lambda u_k\, D_k f(\mathbf{c}_k),$$

con $\mathbf{c}_k$ en el segmento del peldaño. **El hecho decisivo:** como $\mathbf{b}_k \to \mathbf{a}$, también $\mathbf{c}_k \to \mathbf{a}$ cuando $\lambda\to 0$.

**Paso 3 — Aislar el error.** Sumando (8.14) sobre todos los peldaños:

$$f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) = \lambda\sum_{k=1}^n D_k f(\mathbf{c}_k)\,u_k.$$

Por otro lado, la parte lineal candidata es $\nabla f(\mathbf{a})\cdot\mathbf{v} = \lambda\,\nabla f(\mathbf{a})\cdot\mathbf{u} = \lambda\sum_{k=1}^n D_k f(\mathbf{a})\,u_k$. Restando:

$$f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) - \nabla f(\mathbf{a})\cdot\mathbf{v} = \lambda\sum_{k=1}^n \big\{ D_k f(\mathbf{c}_k) - D_k f(\mathbf{a}) \big\}u_k = \|\mathbf{v}\|\,E(\mathbf{a},\mathbf{v}),$$

donde, como $\lambda=\|\mathbf{v}\|$, el coeficiente del error es exactamente

$$E(\mathbf{a},\mathbf{v}) = \sum_{k=1}^n \big\{ D_k f(\mathbf{c}_k) - D_k f(\mathbf{a}) \big\}u_k.$$

**Paso 4 — La continuidad mata el error.** Ahora se ve por qué la hipótesis es *parciales continuas*:

- Cada factor $\{D_k f(\mathbf{c}_k) - D_k f(\mathbf{a})\}$ compara la parcial en el punto intermedio $\mathbf{c}_k$ con la parcial en $\mathbf{a}$.
- Ya vimos que $\mathbf{c}_k \to \mathbf{a}$ cuando $\|\mathbf{v}\|\to 0$.
- **Como cada $D_k f$ es continua en $\mathbf{a}$**, esa diferencia $\to 0$.
- Los $u_k$ son componentes de un vector *unitario*, así que $|u_k|\le 1$: están acotados y no estropean nada.

Por lo tanto $E(\mathbf{a},\mathbf{v}) \to 0$ cuando $\|\mathbf{v}\|\to 0$. Eso es *literalmente* la definición de diferenciable, con $T_{\mathbf{a}}(\mathbf{v}) = \nabla f(\mathbf{a})\cdot\mathbf{v}$ como diferencial. $\blacksquare$

> **Nota sobre la escalera.** El detalle que suele omitirse: los $\mathbf{c}_k$ no están sobre el segmento recto de $\mathbf{a}$ a $\mathbf{a}+\mathbf{v}$, sino sobre los peldaños de la escalera (ya tienen algunas coordenadas movidas y otras no). Da igual para la conclusión —todos $\to\mathbf{a}$—, pero es la razón por la que se usa una suma telescópica y no un solo valor medio.

Y fíjate en lo prometido al inicio: esa parte lineal $\sum_k D_k f(\mathbf{a})\,v_k$ es **exactamente el plano tangente de Taylor** $f(\mathbf{a}) + \nabla f(\mathbf{a})\cdot\mathbf{v}$. La demostración no produjo un objeto nuevo: tomó el plano de Taylor de siempre y probó que, bajo continuidad de las parciales, su error es $o(\|\mathbf{v}\|)$. **El teorema es el certificado del plano de Taylor, no un sustituto.**

### Qué pasa sin continuidad

Si las parciales **no** son continuas, los puntos intermedios $\mathbf{c}_k$ pueden tener pendientes $D_k f(\mathbf{c}_k)$ que **no** se acercan a $D_k f(\mathbf{a})$ al encoger $\mathbf{v}$: el factor $\{D_k f(\mathbf{c}_k) - D_k f(\mathbf{a})\}$ no tiende a $0$ y el error $E(\mathbf{a},\mathbf{v})$ no muere. Ahí vive el contraejemplo $\dfrac{xy^2}{x^2+y^4}$ — las parciales existen en el origen pero son discontinuas ahí, y la función ni siquiera es continua.

## El resumen que disuelve la confusión

No es que "las parciales por sí solas ahora sí sirvan". Es que:

1. Las parciales dan las $n$ direcciones-eje.
2. La **continuidad** extiende ese conocimiento a un entorno completo.
3. El **valor medio** traduce ese entorno a control sobre toda dirección arbitraria.

Por eso $n$ parciales continuas bastan para garantizar lo que infinitas direccionales sueltas no podían. Y por eso las funciones habituales (polinomios, $\sin$, $\cos$, $\exp$, cocientes con denominador no nulo) son diferenciables sin drama: sus parciales son continuas por construcción. El Teorema 8.7 es lo que hace **usable** una teoría que, por lo demás, está llena de contraejemplos delicados.

| Propiedad | ¿Implica diferenciabilidad? |
|---|---|
| Existen las parciales | ❌ No (contraejemplo $xy^2/(x^2+y^4)$) |
| Existen todas las direccionales | ❌ No (ni siquiera continuidad) |
| Existen las parciales **y son continuas** | ✅ Sí (Teorema 8.7, suficiente pero no necesaria) |
| $f$ diferenciable | ⟹ continua, ⟹ existen todas las direccionales, ⟹ existen parciales |
