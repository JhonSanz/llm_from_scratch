import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Datos base
np.random.seed(42)
n_samples = 15
X_pos = np.random.randn(n_samples, 2) + [2, 2]
X_neg = np.random.randn(n_samples, 2) - [2, 2]
X_raw = np.vstack([X_pos, X_neg])
y = np.hstack([np.ones(n_samples), np.zeros(n_samples)])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 2. Configuración de la figura
fig = plt.figure(figsize=(16, 9))
plt.subplots_adjust(bottom=0.25)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

# Malla de alta resolución para el mapa de calor
grid_res = 100
x_range = np.linspace(-6, 6, grid_res)
y_range = np.linspace(-6, 6, grid_res)
xx, yy = np.meshgrid(x_range, y_range)

theta_init = [-0.5, 1.0, 1.0]

# --- PANEL 1 (2D) ---
ax1.set_aspect('equal')
# Inicializamos el heatmap con ceros
heatmap = ax1.imshow(np.zeros((grid_res, grid_res)), extent=[-6, 6, -6, 6], 
                      origin='lower', cmap='RdBu', alpha=0.4, aspect='auto', zorder=0)
heatmap.set_clim(0, 1)

ax1.scatter(X_raw[:n_samples, 0], X_raw[:n_samples, 1], c='blue', edgecolors='k', label='Clase 1', zorder=5)
ax1.scatter(X_raw[n_samples:, 0], X_raw[n_samples:, 1], c='red', edgecolors='k', label='Clase 0', zorder=5)
line_2d, = ax1.plot([], [], 'g-', linewidth=3, label='Frontera (z=0)', zorder=6)

# --- PANEL 2 (3D) ---
# Usamos una malla más ligera para el 3D por rendimiento
xx_3d, yy_3d = np.meshgrid(np.linspace(-6, 6, 40), np.linspace(-6, 6, 40))
surf_container = [ax2.plot_surface(xx_3d, yy_3d, np.zeros(xx_3d.shape), cmap='RdBu', alpha=0.6)]
dots_3d = ax2.scatter(X_raw[:, 0], X_raw[:, 1], np.zeros(len(y)), c=y, cmap='bwr_r', edgecolors='k')

# 3. Sliders
ax_t0 = plt.axes([0.25, 0.12, 0.5, 0.03])
ax_t1 = plt.axes([0.25, 0.08, 0.5, 0.03])
ax_t2 = plt.axes([0.25, 0.04, 0.5, 0.03])

s_t0 = Slider(ax_t0, 'Bias (θ₀)', -10.0, 10.0, valinit=theta_init[0])
s_t1 = Slider(ax_t1, 'Peso x1 (θ₁)', -5.0, 5.0, valinit=theta_init[1])
s_t2 = Slider(ax_t2, 'Peso x2 (θ₂)', -5.0, 5.0, valinit=theta_init[2])

def update(val):
    t0, t1, t2 = s_t0.val, s_t1.val, s_t2.val
    
    # --- Actualizar Mapa de Calor 2D ---
    z_grid = t0 + t1*xx + t2*yy
    probs_grid = sigmoid(z_grid)
    heatmap.set_data(probs_grid) # Esto actualiza los colores del fondo
    
    # --- Actualizar Línea de Frontera ---
    x_vals = np.array([-6, 6])
    if abs(t2) > 1e-5:
        y_vals = -(t1 * x_vals + t0) / t2
        line_2d.set_data(x_vals, y_vals)
        line_2d.set_visible(True)
    else:
        line_2d.set_visible(False)
    
    # --- Actualizar Superficie 3D ---
    probs_3d = sigmoid(t0 + t1*xx_3d + t2*yy_3d)
    surf_container[0].remove()
    surf_container[0] = ax2.plot_surface(xx_3d, yy_3d, probs_3d, cmap='RdBu', 
                                         alpha=0.6, linewidth=0, antialiased=False)
    
    # --- Actualizar Puntos (Altura = Probabilidad) ---
    y_p = sigmoid(t0 + t1*X_raw[:,0] + t2*X_raw[:,1])
    dots_3d._offsets3d = (X_raw[:, 0], X_raw[:, 1], y_p)
    
    ax2.set_zlim(0, 1)
    fig.canvas.draw_idle()

s_t0.on_changed(update)
s_t1.on_changed(update)
s_t2.on_changed(update)

update(None)
plt.show()