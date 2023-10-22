import numpy as np

# Create a 3x3 matrix with different values
matrix = np.array([[2, 4, 6],
                   [1, 3, 5],
                   [8, 7, 9]])

# Calculate and print the sum of columns
column_sum = np.sum(matrix, axis=0)
print("Column Sum:")
print(column_sum)
# Output: [11 14 20]

# Calculate and print the sum of rows
row_sum = np.sum(matrix, axis=1)
print("Row Sum:")
print(row_sum)
# Output: [12  9 24]

