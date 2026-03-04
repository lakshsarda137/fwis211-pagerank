import numpy as np
import matplotlib.pyplot as plt

# Set up the figure
fig = plt.figure(figsize=(15, 10))
fig.suptitle("Match the Space Curves: Round 2", fontsize=16)

# Time domains
t_standard = np.linspace(-5, 5, 1000)
t_pos = np.linspace(0, 15, 1000)
t_trig = np.linspace(0, 2*np.pi, 2000)
t_decay = np.linspace(0, 6, 1000)

# Curve Data (Scrambled completely from A-F)
# Graph 1
x1 = t_standard
y1 = t_standard**2
z1 = np.sin(t_standard)

# Graph 2
x2 = np.sin(3*t_trig)
y2 = np.sin(4*t_trig)
z2 = np.cos(5*t_trig)

# Graph 3
x3 = 3 * np.cos(t_pos)
y3 = np.sin(t_pos)
z3 = t_pos

# Graph 4
x4 = t_pos * np.cos(t_pos)
y4 = t_pos * np.sin(t_pos)
z4 = t_pos**2

# Graph 5
x5 = np.cos(t_trig) * np.sin(5*t_trig)
y5 = np.sin(t_trig) * np.sin(5*t_trig)
z5 = np.cos(5*t_trig)

# Graph 6
x6 = np.exp(-t_decay/2)
y6 = np.exp(-t_decay/2) * np.sin(10*t_decay)
z6 = np.exp(-t_decay/2) * np.cos(10*t_decay)

# Plotting mapping
graphs = [
    (x1, y1, z1, "Graph 1"),
    (x2, y2, z2, "Graph 2"),
    (x3, y3, z3, "Graph 3"),
    (x4, y4, z4, "Graph 4"),
    (x5, y5, z5, "Graph 5"),
    (x6, y6, z6, "Graph 6")
]

for i, (x, y, z, title) in enumerate(graphs):
    ax = fig.add_subplot(2, 3, i+1, projection='3d')
    ax.plot(x, y, z, color='crimson', linewidth=1.2)
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Adjust viewing angle for better 3D perspective
    ax.view_init(elev=25, azim=35)

plt.tight_layout()
plt.show()