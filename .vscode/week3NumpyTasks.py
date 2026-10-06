import numpy as np

#task1
print("\n--- Task 1 ---")

vector = np.random.randint(10,49, 5)
#slicing vector[<from>:<to>:<step>]
print(vector)
reverse = vector[::-1]
print(reverse)


#task2
print("\n--- Task 2 ---")
new_array = np.random.randint(0,10,(5,5))
print(new_array)
max = new_array.max()
min = new_array.min()
print("Max value = ", max)
print("Min value = ", min)

#task3
print("\n--- Task 3 ---")

random = np.random.randint((5,5))
normalized = ((random - random.min()) / (random.max() - random.min()))
print("Normalized matrix = ", normalized)

#task4
print("\n--- Task 4 ---")
matrix1 = np.random.randint(10, size=(5,3))
matrix2 = np.random.randint(10, size=(3,2))
print("matrix1 = ", matrix1)
print("matrix2 = ", matrix2)
multiplied = np.dot(matrix1, matrix2)
print("matrix1 * matrix2 = ", multiplied)


#task5
print("\n--- Task 5 ---")
today = np.datetime64('today', 'D')
y = today - np.datetime64(1, 'D')
tom = today + np.timedelta64(1, 'D')

print("Yesterday:", y)
print("Today:    ", today)
print("Tomorrow: ", tom)


#task6
print("\n--- Task 6 ---")
random = np.random.random(5)*10
print(random)

method1 = np.floor(random)
print(method1)

method2 = random.astype(int)
print(method2)

method3 = np.trunc(random)
print(method3)

method4 = random //1
print(method4)

method5 = random - random % 1
print(method5)

#task7
print("\n--- Task 7 ---")
custom_dtype = np.dtype([
   ('position', [('x', 'f4'), ('y', 'f4')]),
   ('color', [('r', 'u1'),('g', 'u1'),('b', 'u1')] )

])

data = np.zeros(2,dtype=custom_dtype)
print(data)
data[0]['position']=(3.3, 8.0)
data[0]['color']=(255,0,0)

data[1]['position']=(50.5, 7.8)
print(data)



#task8
print("\n--- Task 8 ---")
def generator() :
    num = np.random.randint(1,10,10)
    print(num)

generator()

#task9
print("\n--- Task 9 ---")
A = np.random.random((3,3))
B = np.random.random((3,3))
print("A = ", A)
print("B = ",B)

print("(A == B).all() : " ,(A==B).all())
print("np.array_equal(A,B) : ", np.array_equal(A,B))
print("np.allclose() : ", np.allclose(A,B))

#task10
print("\n--- Task 10 ---")
matrix_list = np.random.random((100, 2))
print("Matrix = ",matrix_list)
for i in range(len(matrix_list)):
    if i < len(matrix_list)-1:
        y_diff = matrix_list[i+1][1] - matrix_list[i][1]
        x_diff = matrix_list[i+1][0] - matrix_list[i][0]
        dist_diff = np.sqrt(abs(y_diff/x_diff))
        print(dist_diff)


#task11
print("\n--- Task 11 ---")
m = np.random.randint(1,10,(3,3))
means = m.mean(axis=1,keepdims=True)
result = m - means
print("Original Matrix = ",m)
print("Mean = ", means)
print("Mean - Matrix = ", result)

#or

A = np.random.random((3,4))

def subtract_mean(row):
    return row - np.mean(row)

result = np.apply_along_axis(subtract_mean, axis =1, arr=A)
print("Original Matrix = ", A)
print("Mean-Subtracted matrix = ", result)


#task12
print("\n--- Task 12 ---")

C = np.random.randint(1,10,(3,3))
sorted = C[:, C[0,:].argsort()]
print("Original Array: ", C)
print("Sorted by column taking into account values in row 0 = ", sorted)

#task13
print("\n--- Task 13 ---")
D = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [7, 8, 9]])
rank = np.linalg.matrix_rank(D)
print("Original Matrix = ", D)
print("Rank of Matrix = ", rank)


#task14
matrix = np.arange(1, 17).reshape(4, 4)

# 1. Define block dimensions
block_rows = 2
block_cols = 2

# 2. Correctly calculate the grid dimensions using floor division (//)
# 4 // 2 = 2 grid rows
grid_rows = matrix.shape[0] // block_rows 
# 4 // 2 = 2 grid cols
grid_cols = matrix.shape[1] // block_cols 

# 3. Reshape using the mathematically correct dimensions: (2, 2, 2, 2)
# 2 * 2 * 2 * 2 = 16 elements, which matches the original matrix size perfectly.
reshaped_matrix = matrix.reshape(grid_rows, block_rows, grid_cols, block_cols)

# 4. Calculate block sum
block_sum_matrix = reshaped_matrix.sum(axis=(1, 3))

print("Matrix:\n", matrix)
print("Block Sum Matrix:\n", block_sum_matrix)
