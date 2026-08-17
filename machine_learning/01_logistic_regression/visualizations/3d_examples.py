import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Preparación de datos 3D
np.random.seed(42)
n_samples = 20
X_pos = np.random.randn(n_samples, 3) + 2
X_neg = np.random.randn(n_samples, 3) - 2
X_raw = np.vstack([X_pos, X_neg])
y = np.hstack([np.ones(n_samples), np.zeros(n_samples)])
X = np.column_stack([np.ones(2 * n_samples), X_raw]) # Bias + x1, x2, x3

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, theta):
    h = sigmoid(np.dot(X, theta))
    epsilon = 1e-15
    h = np.clip(h, epsilon, 1 - epsilon)
    return (-1/len(y)) * (np.dot(y, np.log(h)) + np.dot((1-y), np.log(1-h)))

# 2. Entrenamiento (θ₀, θ₁, θ₂, θ₃)
theta = np.array([1, 0.5, 0, -0.5]) 
lr = 0.2
history = []
for i in range(50):
    cost = compute_cost(X, y, theta)
    history.append((theta.copy(), cost))
    gradient = np.dot(X.T, (sigmoid(np.dot(X, theta)) - y)) / len(y)
    theta -= lr * gradient

# 3. Animación Triple 3D
fig = plt.figure(figsize=(22, 8))
ax1 = fig.add_subplot(131, projection='3d') # Nube de puntos + Plano
ax2 = fig.add_subplot(132, projection='3d') # Trayectoria de Pesos
ax3 = fig.add_subplot(133)                  # Curva de Costo

# Malla para el plano de decisión (Panel 1)
xm, ym = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

def update(frame):
    [ax.clear() for ax in [ax1, ax2, ax3]]
    curr_theta, curr_cost = history[frame]
    
    # --- PANEL 1: FRONTERA DE DECISIÓN (PLANO) ---
    ax1.scatter(X_raw[:n_samples, 0], X_raw[:n_samples, 1], X_raw[:n_samples, 2], c='blue', label='Clase 1')
    ax1.scatter(X_raw[n_samples:, 0], X_raw[n_samples:, 1], X_raw[n_samples:, 2], c='red', label='Clase 0')
    
    # Plano: t0 + t1*x + t2*y + t3*z = 0 -> z = -(t0 + t1*x + t2*y) / t3
    if abs(curr_theta[3]) > 0.01:
        zm = -(curr_theta[0] + curr_theta[1]*xm + curr_theta[2]*ym) / curr_theta[3]
        ax1.plot_surface(xm, ym, zm, alpha=0.2, color='green')
    
    ax1.set_title("Frontera de Decisión (Hiperplano)")
    ax1.set_xlim(-5, 5); ax1.set_ylim(-5, 5); ax1.set_zlim(-5, 5)

    # --- PANEL 2: TRAYECTORIA EN ESPACIO DE PESOS ---
    thetas_hist = np.array([h[0] for h in history[:frame+1]])
    ax2.plot(thetas_hist[:, 1], thetas_hist[:, 2], thetas_hist[:, 3], 'b-', alpha=0.6)
    ax2.scatter(curr_theta[1], curr_theta[2], curr_theta[3], color='red', s=50)
    ax2.set_title("Descenso del Gradiente (θ₁, θ₂, θ₃)")
    ax2.set_xlabel("θ₁"); ax2.set_ylabel("θ₂"); ax2.set_zlabel("θ₃")

    # --- PANEL 3: EVOLUCIÓN DEL COSTO J ---
    costs = [h[1] for h in history[:frame+1]]
    ax3.plot(costs, 'r-')
    ax3.set_title(f"Costo J: {curr_cost:.4f}")
    ax3.set_xlabel("Iteración"); ax3.set_ylabel("J(θ)")
    
    # Cuadro de texto
    text_str = (f"θ₀(bias): {curr_theta[0]:.2f}\n"
                f"θ₁: {curr_theta[1]:.2f}\n"
                f"θ₂: {curr_theta[2]:.2f}\n"
                f"θ₃: {curr_theta[3]:.2f}")
    ax3.text(0.5, 0.8, text_str, transform=ax3.transAxes, bbox=dict(facecolor='white', alpha=0.5))

    return fig,

ani = FuncAnimation(fig, update, frames=len(history), interval=500, repeat=False)
plt.show()