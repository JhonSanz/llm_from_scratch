import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Datos en 3D
np.random.seed(42)
n = 20
X_pos = np.random.randn(n, 3) + [2, 2, 2]
X_neg = np.random.randn(n, 3) - [2, 2, 2]
X_raw = np.vstack([X_pos, X_neg])
y = np.hstack([np.ones(n), np.zeros(n)])

# 2. Configuración 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

# Malla para el plano de decisión
xx, yy = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

# Parámetros iniciales
theta = [0.0, 1.0, 1.0, 1.0]

def get_z_plane(t0, t1, t2, t3, x, y):
    # Despeje de theta0 + t1*x + t2*y + t3*z = 0 -> z = -(t0 + t1*x + t2*y) / t3
    if abs(t3) < 0.01: t3 = 0.01
    return -(t0 + t1*x + t2*y) / t3

# Dibujo inicial
plane_z = get_z_plane(*theta, xx, yy)
surf = [ax.plot_surface(xx, yy, plane_z, alpha=0.3, color='green')]
scat = ax.scatter(X_raw[:,0], X_raw[:,1], X_raw[:,2], c=y, cmap='bwr', s=50, edgecolors='k')

ax.set_xlim(-5, 5); ax.set_ylim(-5, 5); ax.set_zlim(-5, 5)
ax.set_title("Frontera de Decisión 3D (Plano)")

# Sliders
ax_t0 = plt.axes([0.2, 0.15, 0.6, 0.03])
ax_t1 = plt.axes([0.2, 0.11, 0.6, 0.03])
ax_t2 = plt.axes([0.2, 0.07, 0.6, 0.03])
ax_t3 = plt.axes([0.2, 0.03, 0.6, 0.03])

s0 = Slider(ax_t0, 'Bias', -5, 5, valinit=0)
s1 = Slider(ax_t1, 'θ₁ (x)', -2, 2, valinit=1)
s2 = Slider(ax_t2, 'θ₂ (y)', -2, 2, valinit=1)
s3 = Slider(ax_t3, 'θ₃ (z)', -2, 2, valinit=1)

def update(val):
    t0, t1, t2, t3 = s0.val, s1.val, s2.val, s3.val
    surf[0].remove()
    z_p = get_z_plane(t0, t1, t2, t3, xx, yy)
    surf[0] = ax.plot_surface(xx, yy, z_p, alpha=0.3, color='green')
    fig.canvas.draw_idle()

s0.on_changed(update); s1.on_changed(update); s2.on_changed(update); s3.on_changed(update)
plt.show()