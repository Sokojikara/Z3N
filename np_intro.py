import numpy as np


### Array Creation

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array: ", array)

zeros = np.zeros((3, 3))
print("Zeros: ", zeros)

ones = np.ones((3, 3))
print("Ones: ", ones)

range_array = np.arange(0, 10, 2)
print("Range: ", range_array)

random_array = np.random.randint(0, 10, size=(3, 3))
print("Random: ", random_array)

linspace_array = np.linspace(0, 10, num=6)
print("Linspace: ", linspace_array)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2d Array: ", array_2d)

array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("3d Array: ", array_3d)


### Array Attributes

print("Shape: ", array.shape)
print("Dimensions: ", array.ndim)
print("Size: ", array.size)
print("Type: ", array.dtype)


### Array Indexing

print("First element: ", array[0])
print("Last element: ", array[-1])


### Array Slicing

print("First three elements: ", array[:3])
print("Last three elements: ", array[-3:])
print("Middle elements: ", array[3:6])


### Array Operations

array = np.sqrt(array)
print("Square root: ", array)

array = np.exp(array)
print("Exponential: ", array)

array = np.sin(array)
print("Sine: ", array)

array = np.cos(array)
print("Cosine: ", array)

array = np.tan(array)
print("Tangent: ", array)

array = np.log(array)
print("Logarithm: ", array)


### Array Math

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

addition = np.add(array, array)
print("Addition: ", addition)

subtraction = np.subtract(array, array)
print("Subtraction: ", subtraction)

multiplication = np.multiply(array, array)
print("Multiplication: ", multiplication)

division = np.divide(array, array)
print("Division: ", division)

exponentiation = np.power(array, array)
print("Exponentiation: ", exponentiation)

total = np.sum(array)
print("Total: ", total)

minimum = np.min(array)
print("Minimum: ", minimum)

maximum = np.max(array)
print("Maximum: ", maximum)

mean = np.mean(array)
print("Mean: ", mean)

median = np.median(array)
print("Median: ", median)


