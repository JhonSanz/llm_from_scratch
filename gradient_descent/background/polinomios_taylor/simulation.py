import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# 1. Configuración de datos base
x = np.linspace(-10, 10, 500)
y_real = np.sin(x)

def get_taylor_term_string(i):
    """Genera la representación en texto del término i-ésimo"""
    exponent = 2 * i + 1
    sign = "+" if i % 2 == 0 else "-"
    # Simplificación estética para el primer término
    if i == 0:
        return "x"
    
    return f" {sign} \\frac{{x^{{{exponent}}}}}{{{exponent}!}}"

# 2. Configuración de la figura
fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(x, y_real, label='sin(x) Real', color='black', lw=1.5, linestyle='--')
line, = ax.plot([], [], label='Aproximación Taylor', color='red', lw=2)

# Texto para la fórmula (usaremos coordenadas relativas al eje)
formula_text = ax.text(0.05, 0.05, '', transform=ax.transAxes, fontsize=12,
                       verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_ylim(-2.5, 2.5)
ax.set_xlim(-10, 10)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')

# 3. Función de actualización
current_formula = "P(x) = "

def update(frame):
    global current_formula
    n_terms = frame + 1
    
    # Calcular el polinomio hasta el término actual
    y_approx = np.zeros_like(x)
    temp_formula = "P(x) \\approx "
    
    for i in range(n_terms):
        exponent = 2 * i + 1
        coef = ((-1)**i) / math.factorial(exponent)
        y_approx += coef * (x**exponent)
        temp_formula += get_taylor_term_string(i)

    # Actualizar línea y texto
    line.set_data(x, y_approx)
    formula_text.set_text(f"${temp_formula}$")
    ax.set_title(f"Aproximación con {n_terms} términos (Grado {2*frame+1})")
    
    return line, formula_text

# 4. Animación
# Aumentamos a 10 términos para ver cómo se expande la precisión
ani = FuncAnimation(fig, update, frames=10, interval=1500, blit=True)

plt.show()