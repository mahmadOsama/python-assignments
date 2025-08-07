import numpy as np

# Part 1: Creating NumPy Arrays
print("Part 1: Creating NumPy Arrays")
print("1. Using Built-in Methods:")

# Array from 0 to 20 with step 2
numbers = np.arange(0, 21, 2)
print("Array from 0 to 20 with step 2:", numbers)

# 3x3 identity matrix  
identity = np.eye(3)
print("3x3 identity matrix:")
print(identity)

# 4x4 array of ones
ones_matrix = np.ones((4, 4))
print("4x4 array filled with ones:")
print(ones_matrix)

# 10 equally spaced numbers between 5 and 50
spaced_nums = np.linspace(5, 50, 10)
print("10 equally spaced numbers between 5 and 50:", spaced_nums)

print("\n2. Creating Arrays from Lists:")

# Convert Python list to NumPy array
my_list = [10, 20, 30, 40, 50]
array_from_list = np.array(my_list)
print("NumPy array from list:", array_from_list)

# 3x3 random matrices
print("3x3 matrix using rand():")
rand_matrix = np.random.rand(3, 3)
print(rand_matrix)

print("3x3 matrix using randn():")
randn_matrix = np.random.randn(3, 3)
print(randn_matrix)

print("3x3 matrix using randint():")
randint_matrix = np.random.randint(0, 10, (3, 3))
print(randint_matrix)

print("\n3. Array Attributes:")
print("Shape of ones_matrix:", ones_matrix.shape)
print("Size of ones_matrix:", ones_matrix.size) 
print("Data type of ones_matrix:", ones_matrix.dtype)

# Part 2: Indexing and Selection
print("\n" + "="*50)
print("Part 2: Indexing and Selection")
print("1. Basic Indexing and Selection:")

# Create array
arr = np.array([5, 10, 15, 20, 25, 30])
print("Original array:", arr)

# First element
print("First element:", arr[0])

# Last three elements
print("Last three elements:", arr[-3:])

# Elements at index 1 to 4
print("Elements at index 1 to 4:", arr[1:5])

print("\n2. Slicing and Views:")

# Create 3x3 matrix
matrix = np.arange(1, 10).reshape(3, 3)
print("3x3 matrix:")
print(matrix)

# Second row
print("Second row:", matrix[1])

# First two columns
print("First two columns:")
print(matrix[:, :2])

# 2x2 sub-matrix
print("2x2 sub-matrix:")
print(matrix[:2, :2])

print("\n3. Broadcasting:")

# Create 3x3 matrix and add 10
test_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix:")
print(test_matrix)

# Add 10 to every element
result1 = test_matrix + 10
print("After adding 10:")
print(result1)

# Multiply first column by 2
test_matrix[:, 0] = test_matrix[:, 0] * 2
print("After multiplying first column by 2:")
print(test_matrix)

print("\n4. Copying Arrays:")

# Original array
original = np.array([1, 2, 3, 4, 5])
print("Original array:", original)

# Shallow copy (view)
shallow_copy = original
shallow_copy[0] = 99
print("After modifying shallow copy:")
print("Original:", original)
print("Shallow copy:", shallow_copy)

# Reset for deep copy demo
original = np.array([1, 2, 3, 4, 5])
deep_copy = original.copy()
deep_copy[0] = 99
print("After modifying deep copy:")
print("Original:", original)
print("Deep copy:", deep_copy)

print("\n5. Fancy Indexing:")

# Create array and select specific indices
arr2 = np.arange(10, 101, 10)
print("Array:", arr2)
selected = arr2[[0, 3, 5]]
print("Elements at indices [0, 3, 5]:", selected)

# Part 3: NumPy Operations
print("\n" + "="*50)
print("Part 3: NumPy Operations")
print("1. Mathematical Functions:")

# Array for mathematical operations
math_array = np.array([3, 7, 2, 9, 12, 5, 10])
print("Array:", math_array)

# Find maximum and minimum values
print("Maximum value:", np.max(math_array))
print("Minimum value:", np.min(math_array))

# Find indices of max and min
print("Index of maximum:", np.argmax(math_array))
print("Index of minimum:", np.argmin(math_array))

print("\n2. Universal Array Functions:")

# Array for universal functions
func_array = np.array([1, 2, 3, 4, 5])
print("Original array:", func_array)

# Apply different mathematical functions
print("Square root:", np.sqrt(func_array))
print("Exponential:", np.exp(func_array))
print("Sine:", np.sin(func_array))
print("Natural logarithm:", np.log(func_array))