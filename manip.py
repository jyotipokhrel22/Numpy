import numpy as np

# Array manipulation
array = np.random.randint(0, 10, (2,3))
print(array)
print(array.shape)

# Transpose 
trans = np.transpose(array)
print(trans)
print(trans.shape)

# Another way
trans2 = array.T
print(trans2)
print(trans2.shape)

# Reshaping an array
a = np.random.randint(0, 10, (2,3))
print(a)
print(a.shape)

b = a.reshape(3,2)
print(b)
print(b.shape)