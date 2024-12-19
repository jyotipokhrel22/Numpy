# Mathematical operations on an numpy array:

import numpy as np

a = np.random.randint(0, 10, (3,3))
b = np.random.randint(10, 20, (3,3))

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Another way

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

