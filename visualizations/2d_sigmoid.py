import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Datos y Funciones Base
np.random.seed(101)
n_samples = 15
X_pos = np.random.randn(n_samples, 2) + 1.5
X_neg = np.random.randn(n_samples, 2) - 1.5
X_raw = np.vstack([X_pos, X_neg])
y = np.hstack([np.ones(n_samples), np.zeros(n_samples)])
X = np.column_stack([np.ones(2 * n_samples), X_raw])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost_mse(X, y, theta):
    h = sigmoid(np.dot(X, theta))
    return np.mean((h - y)**2)

# 2. Entrenamiento con inicialización extrema (Saturación)
# Pesos grandes y opuestos para forzar a la sigmoide a estar en zona plana
theta = np.array([1.0, -2.0, -2.0]) 
lr = 2.0 
history = []
grad_norms = []

for i in range(100):
    h = sigmoid(np.dot(X, theta))
    cost = compute_cost_mse(X, y, theta)
    
    # Derivada MSE: (h-y) * h(1-h) * X
    gradient = np.dot(X.T, (h - y) * h * (1 - h)) / len(y)
    grad_norm = np.linalg.norm(gradient)
    
    history.append((theta.copy(), cost))
    grad_norms.append(grad_norm)
    theta -= lr * gradient

# 3. Configuración de 4 Gráficos (2x2)
fig = plt.figure(figsize=(16, 12))
ax1 = fig.add_subplot(221)                  # 2D Frontera
ax2 = fig.add_subplot(222, projection='3d') # Sigmoide 3D
ax3 = fig.add_subplot(223, projection='3d') # Superficie Costo MSE (La bolita)
ax4 = fig.add_subplot(224)                  # Magnitud Gradiente

# Malla para superficies
xx, yy = np.meshgrid(np.linspace(-10, 10, 40), np.linspace(-10, 10, 40))
grid_points = np.c_[np.ones(xx.ravel().shape), xx.ravel(), yy.ravel()]

# Ampliamos el rango para ver más porción de la superficie
# t1_v = np.linspace(-15, 15, 60) 
# t2_v = np.linspace(-15, 15, 60)
# T1, T2 = np.meshgrid(t1_v, t2_v)
t1_v, t2_v = np.linspace(-10, 10, 40), np.linspace(-10, 10, 40)
T1, T2 = np.meshgrid(t1_v, t2_v)

# Pre-calculamos superficie de costo (Panel 3)
Z_cost_mse = np.array([compute_cost_mse(X, y, np.array([history[0][0][0], t1, t2])) 
                      for t1, t2 in zip(np.ravel(T1), np.ravel(T2))]).reshape(T1.shape)

def update(frame):
    [ax.clear() for ax in [ax1, ax2, ax3, ax4]]
    curr_theta, curr_cost = history[frame]
    probs = sigmoid(np.dot(grid_points, curr_theta)).reshape(xx.shape)
    
    # PANEL 1: Frontera 2D
    ax1.contourf(xx, yy, probs, levels=20, cmap='RdBu', alpha=0.3)
    ax1.scatter(X_raw[:n_samples, 0], X_raw[:n_samples, 1], c='blue', edgecolors='k', label='Clase 1')
    ax1.scatter(X_raw[n_samples:, 0], X_raw[n_samples:, 1], c='red', edgecolors='k', label='Clase 0')
    x_l = np.array([-5, 5])
    if abs(curr_theta[2]) > 1e-5:
        y_l = -(curr_theta[1]*x_l + curr_theta[0])/curr_theta[2]
        ax1.plot(x_l, y_l, 'g-', linewidth=3)
    ax1.set_title("Frontera de Decisión (MSE)")
    ax1.set_xlim(-5, 5); ax1.set_ylim(-5, 5)

    # PANEL 2: Sigmoide 3D (Saturación)
    ax2.plot_surface(xx, yy, probs, cmap='RdBu', alpha=0.6)
    ax2.set_title("Sigmoide h(x): Zona Plana")
    ax2.set_zlim(0, 1)

    # PANEL 3: Superficie de Costo + Bolita
    ax3.plot_surface(T1, T2, Z_cost_mse, alpha=0.4, cmap='inferno')
    ax3.scatter(curr_theta[1], curr_theta[2], curr_cost, color='cyan', s=150, edgecolors='k', depthshade=False)
    ax3.set_title("Paisaje MSE: La bolita no cae")
    ax3.set_xlabel('θ₁'); ax3.set_ylabel('θ₂')

    # PANEL 4: Magnitud del Gradiente
    ax4.plot(range(frame), grad_norms[:frame], color='red', linewidth=2)
    ax4.set_title("¿Por qué no se mueve? Gradiente ≈ 0")
    ax4.set_xlabel("Iteración"); ax4.set_ylabel("||Gradiente||")
    ax4.set_xlim(0, 100); ax4.set_ylim(0, max(grad_norms)*1.2 if grad_norms else 1)
    ax4.grid(True, alpha=0.2)

    # Info Text
    text_info = f"Iter: {frame}\nCosto: {curr_cost:.5f}\nGrad: {grad_norms[frame]:.7f}"
    ax1.text(0.05, 0.95, text_info, transform=ax1.transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), family='monospace')

    return fig,

ani = FuncAnimation(fig, update, frames=len(history), interval=150, repeat=True)
plt.tight_layout()
plt.show()