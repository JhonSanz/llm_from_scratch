import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Preparación de datos (Mezclados en el origen)
np.random.seed(42)
n_samples = 20

X_pos = np.random.randn(n_samples, 2) + 2
X_neg = np.random.randn(n_samples, 2) - 2
X_raw = np.vstack([X_pos, X_neg])

# X_raw = np.random.randn(2 * n_samples, 2)
y = np.hstack([np.ones(n_samples), np.zeros(n_samples)])
X = np.column_stack([np.ones(2 * n_samples), X_raw])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, theta):
    h = sigmoid(np.dot(X, theta))
    epsilon = 1e-15
    h = np.clip(h, epsilon, 1 - epsilon)
    return (-1/len(y)) * (np.dot(y, np.log(h)) + np.dot((1-y), np.log(1-h)))

# 2. Entrenamiento (Gradiente Descendente)
theta = np.array([-0.5, -2.0, -2.0]) 
lr = 0.3
history = []
for i in range(50):
    cost = compute_cost(X, y, theta)
    history.append((theta.copy(), cost))
    gradient = np.dot(X.T, (sigmoid(np.dot(X, theta)) - y)) / len(y)
    theta -= lr * gradient

# 3. Configuración de la Animación Triple
fig = plt.figure(figsize=(22, 7))
ax1 = fig.add_subplot(131)                   # Mapa 2D con Recta
ax2 = fig.add_subplot(132, projection='3d')  # Superficie Sigmoide 3D
ax3 = fig.add_subplot(133, projection='3d')  # Superficie de Costo

# Malla fina para las superficies
xx, yy = np.meshgrid(np.linspace(-5, 5, 40), np.linspace(-5, 5, 40))
grid_points = np.c_[np.ones(xx.ravel().shape), xx.ravel(), yy.ravel()]

# Pre-calculamos superficie de costo (Panel Derecho)
t1_v, t2_v = np.linspace(-10, 10, 10), np.linspace(-10, 10, 10)
T1, T2 = np.meshgrid(t1_v, t2_v)
Z_cost = np.array([compute_cost(X, y, np.array([history[-1][0][0], t1, t2])) 
                  for t1, t2 in zip(np.ravel(T1), np.ravel(T2))]).reshape(T1.shape)

def update(frame):
    [ax.clear() for ax in [ax1, ax2, ax3]]
    curr_theta, curr_cost = history[frame]
    
    # --- PANEL 1: MAPA 2D + RECTA + THETAS ---
    ax1.set_aspect('equal', adjustable='box')
    probs = sigmoid(np.dot(grid_points, curr_theta)).reshape(xx.shape)
    ax1.contourf(xx, yy, probs, levels=20, cmap='RdBu', alpha=0.3)
    ax1.scatter(X_raw[:n_samples, 0], X_raw[:n_samples, 1], c='blue', edgecolors='k', label='Clase 1')
    ax1.scatter(X_raw[n_samples:, 0], X_raw[n_samples:, 1], c='red', edgecolors='k', label='Clase 0')
    
    # Recta de Decisión (h=0.5)
    x_line = np.array([-5, 5])
    if curr_theta[2] != 0:
        y_line = -(curr_theta[1] * x_line + curr_theta[0]) / curr_theta[2]
        ax1.plot(x_line, y_line, 'g-', linewidth=3, label='Frontera')
    
    ax1.set_xlim(-5, 5); ax1.set_ylim(-5, 5)
    ax1.set_title("Frontera de Decisión y Probabilidades")
    
    # Cuadro de texto con parámetros (Tu petición)
    text_str = (f"Iteración: {frame}\n"
                f"θ₀ (bias): {curr_theta[0]:.3f}\n"
                f"θ₁ (w1)  : {curr_theta[1]:.3f}\n"
                f"θ₂ (w2)  : {curr_theta[2]:.3f}\n"
                f"Costo J  : {curr_cost:.4f}")
    ax1.text(0.05, 0.95, text_str, transform=ax1.transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9), family='monospace')

    # --- PANEL 2: SUPERFICIE SIGMOIDE 3D ---
    ax2.plot_surface(xx, yy, probs, cmap='RdBu', alpha=0.6, antialiased=True)
    y_pred = sigmoid(np.dot(X, curr_theta))
    ax2.scatter(X_raw[:, 0], X_raw[:, 1], y_pred, c=y, cmap='bwr_r', s=50, edgecolors='k')
    ax2.set_title("Evolución de la Sigmoide h_θ(x)")
    ax2.set_zlim(0, 1)
    ax2.set_xlabel('x1'); ax2.set_ylabel('x2'); ax2.set_zlabel('Probabilidad')

    # --- PANEL 3: SUPERFICIE DE COSTO ---
    ax3.plot_surface(T1, T2, Z_cost, alpha=0.3, cmap='viridis')
    ax3.scatter(curr_theta[1], curr_theta[2], curr_cost, color='red', s=100)
    ax3.set_title("Paisaje del Costo (Convexo)")
    ax3.set_xlabel('θ₁'); ax3.set_ylabel('θ₂')
    
    return fig,

ani = FuncAnimation(fig, update, frames=len(history), interval=500, repeat=False)
plt.show()