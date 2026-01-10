import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Datos en 1D
np.random.seed(42)
n_samples = 15
x0 = np.random.normal(-2, 1, n_samples)
x1 = np.random.normal(2, 1, n_samples)
X_raw = np.concatenate([x0, x1])
y = np.concatenate([np.zeros(n_samples), np.ones(n_samples)])
X = np.column_stack([np.ones(2*n_samples), X_raw])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, theta):
    h = sigmoid(np.dot(X, theta))
    epsilon = 1e-15
    h = np.clip(h, epsilon, 1 - epsilon)
    return (-1/len(y)) * (np.dot(y, np.log(h)) + np.dot((1-y), np.log(1-h)))

# 2. Entrenamiento
theta = np.array([0.0, 0.1]) 
lr = 0.5
history = []
for i in range(60):
    cost = compute_cost(X, y, theta)
    history.append((theta.copy(), cost))
    gradient = np.dot(X.T, (sigmoid(np.dot(X, theta)) - y)) / len(y)
    theta -= lr * gradient

# 3. Configuración de Animación
fig = plt.figure(figsize=(22, 7))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133, projection='3d')

t1_range = np.linspace(-1, 5, 50)
t0_range = np.linspace(-3, 3, 50)
T0, T1 = np.meshgrid(t0_range, t1_range)
Z_cost = np.array([compute_cost(X, y, np.array([t0, t1])) 
                  for t0, t1 in zip(np.ravel(T0), np.ravel(T1))]).reshape(T0.shape)

def update(frame):
    [ax.clear() for ax in [ax1, ax2, ax3]]
    curr_theta, curr_cost = history[frame]
    
    # --- PANEL 1: MAPA DE CALOR CUADRADO ---
    # Forzamos aspecto igual para que se vea como Geogebra
    ax1.set_aspect('equal', adjustable='box')
    
    line_x = np.linspace(-6, 6, 500)
    line_y = sigmoid(curr_theta[0] + curr_theta[1] * line_x)
    
    # Fondo de calor
    heatmap_data = line_y.reshape(1, -1)
    ax1.imshow(heatmap_data, extent=[-6, 6, -0.05, 1.05], aspect='auto', 
               cmap='RdBu', alpha=0.3, origin='lower', zorder=0)
    
    ax1.plot(line_x, line_y, color='green', linewidth=3, label='Sigmoide h_θ(x)')
    ax1.scatter(X_raw, y, c=y, cmap='bwr_r', edgecolors='k', s=60, zorder=5)
    
    if curr_theta[1] != 0:
        db = -curr_theta[0] / curr_theta[1]
        ax1.axvline(db, color='black', linestyle='--', alpha=0.8, label=f'Frontera: {db:.2f}')
    
    # Parámetros theta en pantalla
    text_str = (f"Iteración: {frame}\n"
                f"θ₀ (bias): {curr_theta[0]:.3f}\n"
                f"θ₁ (peso): {curr_theta[1]:.3f}\n"
                f"Costo J  : {curr_cost:.4f}")
    ax1.text(0.05, 0.95, text_str, transform=ax1.transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9), family='monospace')

    ax1.set_title("Clasificación 1D (Escala Cuadrada)")
    ax1.set_xlim(-6, 6); ax1.set_ylim(-0.05, 1.05)
    ax1.legend(loc='lower right')

    # --- PANEL 2 y 3: COSTO ---
    costs_t1 = [compute_cost(X, y, np.array([curr_theta[0], t1])) for t1 in t1_range]
    ax2.plot(t1_range, costs_t1, color='gray', alpha=0.5)
    ax2.scatter(curr_theta[1], curr_cost, color='red', s=100)
    ax2.set_title(f"Costo vs θ₁")
    
    ax3.plot_surface(T0, T1, Z_cost, cmap='viridis', alpha=0.3)
    ax3.scatter(curr_theta[0], curr_theta[1], curr_cost, color='red', s=100)
    ax3.view_init(elev=20, azim=-45)
    
    return fig,

ani = FuncAnimation(fig, update, frames=len(history), interval=100, repeat=False)
plt.show()