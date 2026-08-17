import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Datos base (fijos para el experimento)
np.random.seed(42)
x0 = np.random.normal(-2, 0.8, 10)
x1 = np.random.normal(2, 0.8, 10)
X_raw = np.concatenate([x0, x1])
y = np.concatenate([np.zeros(10), np.ones(10)])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 3. Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25) # Espacio para los sliders
ax.set_aspect('equal', adjustable='box')

# Elementos iniciales
line_x = np.linspace(-6, 6, 500)
theta_init = [0.0, 1.0] # Bias y Peso inicial
z = theta_init[0] + theta_init[1] * line_x
line_y = sigmoid(z)

# Dibujo inicial
heatmap = ax.imshow(line_y.reshape(1, -1), extent=[-6, 6, -0.05, 1.05], 
                    aspect='auto', cmap='RdBu', alpha=0.3, origin='lower')
curve, = ax.plot(line_x, line_y, color='green', linewidth=3)
dots = ax.scatter(X_raw, y, c=y, cmap='bwr_r', edgecolors='k', s=60, zorder=5)
v_line = ax.axvline(-theta_init[0]/theta_init[1], color='black', linestyle='--')

# Texto de información
txt = ax.text(0.05, 0.95, "", transform=ax.transAxes, verticalalignment='top',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.9), family='monospace')

ax.set_xlim(-6, 6)
ax.set_ylim(-0.05, 1.05)
ax.set_title("Modo Manual: Controla los Parámetros θ")

# 4. Creación de Sliders
ax_theta0 = plt.axes([0.2, 0.1, 0.6, 0.03])
ax_theta1 = plt.axes([0.2, 0.05, 0.6, 0.03])

s_theta0 = Slider(ax_theta0, 'Bias (θ₀)', -5.0, 5.0, valinit=theta_init[0])
s_theta1 = Slider(ax_theta1, 'Peso (θ₁)', 0.1, 10.0, valinit=theta_init[1])

def update(val):
    t0 = s_theta0.val
    t1 = s_theta1.val
    
    # Recalcular curva y frontera
    new_z = t0 + t1 * line_x
    new_y = sigmoid(new_z)
    db = -t0 / t1
    
    # Actualizar visualización
    curve.set_ydata(new_y)
    v_line.set_xdata([db, db])
    heatmap.set_data(new_y.reshape(1, -1))
    
    # Actualizar texto
    txt.set_text(f"θ₀ (bias): {t0:.2f}\nθ₁ (peso): {t1:.2f}\nFrontera: {db:.2f}")
    fig.canvas.draw_idle()

s_theta0.on_changed(update)
s_theta1.on_changed(update)

update(None) # Inicializar texto
plt.show()