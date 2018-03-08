import numpy as np

a = np.array([[1], [2]])

b = np.array([[2, 3], [3, 3]])

print(a)
print(b)
print(np.shape(a), np.shape(b))
print(np.matmul(a, b))