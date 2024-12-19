import numpy as np
# 1d array
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.shape) #gives no of rows and columns in that np array

# 2d array
b = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(b)
print(b.shape)

c = np.array([(1.77, 2.56, 3.78, 4.90), (5.76, 6.53, 7.76, 8.32)], dtype=float) #dtype=float is optional here but can be used for b, stating datatype is float
print(c)

# numpy array of zeros
x = np.zeros((4,5))
print(x)

# numpy array of zeros
y = np.ones((4,5))
print(y)

# numpy array of a particular value
z = np.full((3,2), 9)
print(z)

# identity matrix
a = np.eye(3)
print(a)

# create numpy array with random values (0 to 1)
b = np.random.random((3,4))
print(b)

# create a numpy array with random values within a specific range
c = np.random.randint(10, 100, (3,5)) # (starting point, ending point, shape of the array)
print(c)

# create a numpy array of evenly spaced values
d = np.linspace(10, 30, 5) # (starting point, ending point, no. of values needed)
print(d)

e = np.arange(10, 30, 5) # (starting point, ending point, specify the step to jump)
print(e)

# convert a list to a numpy array
list = [10 , 20, 30, 40, 50]

np_array = np.asarray(list)
print(np_array)
print(type(np_array))

