import numpy as np

# Define the matrices
M = np.array([
    [0, 0, 1, 0.5],
    [1/3, 0, 0, 0],
    [1/3, 0.5, 0, 0.5],
    [1/3, 0.5, 0, 0]
])

E = np.ones((4, 4)) * 0.25

d = 0.85

# Calculate G
G = d * M + (1 - d) * E

print("Matrix G:")
print(G)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(G)

# Find the index of the eigenvalue closest to 1
index = np.argmin(np.abs(eigenvalues - 1))

eigenvalue = eigenvalues[index]
eigenvector = eigenvectors[:, index]

# Normalize the eigenvector so the sum of elements is 1 (probability distribution)
steady_state_vector = eigenvector / np.sum(eigenvector)

# Take the real part (since G is real and positive, the principal eigenvector is real)
steady_state_vector = np.real(steady_state_vector)

print("\nEigenvalue closest to 1:", eigenvalue)
print("\nSteady State Vector (Eigenvector for lambda=1):")
print(steady_state_vector)

# Verify G * v = v
print("\nVerification (G * v):")
print(np.dot(G, steady_state_vector))
