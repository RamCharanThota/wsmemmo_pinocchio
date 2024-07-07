import numpy as np

def null_space(A, tol=1e-15):
    U, S, Vt = np.linalg.svd(A)
    null_mask = (S <= tol)
    null_space = Vt.T[:, null_mask]
    return null_space

# Example matrices
A1 = np.array([[1, 2], [3, 4]])
b1 = np.array([5, 6])
A2 = np.array([[7, 8], [9, 10]])
b2 = np.array([11, 12])

# Initial Method: Projection of the Second Task

# Step 1: Solve A1 * x = b1 for a particular solution and null space
x_p, _, _, _ = np.linalg.lstsq(A1, b1, rcond=None)
N = null_space(A1)

# Step 2: Project A2 * x = b2 into the null space of A1
A2_prime = A2 @ N
b2_prime = b2 - A2 @ x_p

# Step 3: Solve the projected system
z, _, _, _ = np.linalg.lstsq(A2_prime, b2_prime, rcond=None)

# Step 4: Combine the solutions
x_initial_method = x_p + N @ z

print("Final solution using the initial method x:", x_initial_method)

# Your Method: Projecting the Solution of the Second Task

# Step 1: Solve A2 * x = b2
x2 = np.linalg.lstsq(A2, b2, rcond=None)[0]

# Step 2: Find the null space of A1
N = null_space(A1)

# Step 3: Project x2 onto the null space of A1
PN = N @ np.linalg.inv(N.T @ N) @ N.T
x2_null = PN @ x2

# Step 4: Solve A1 * x = b1 for a particular solution
x_p, _, _, _ = np.linalg.lstsq(A1, b1, rcond=None)

# Step 5: Combine the solutions
x_your_method = x_p + x2_null

print("Final solution using your method x:", x_your_method)
