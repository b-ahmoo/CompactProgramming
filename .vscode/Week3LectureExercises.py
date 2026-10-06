import numpy as np 
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math

#ndarray.dtype an object describing the type of the elements in the array. 
# One can create or specify dtype’s using standard Python types. 
# Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

a=np.array([1,2,3,4]) 
#print(a.dtype)

a = np.random.random((1,20))
print(a)

a=np.array([1.2,2.2,3.2,4.2]) 
#print(a.dtype)

L = [1,2,3]
L1= [4,5,6]
# ab = np.array([(1,2,3),(5,4,3),(L),(L1)]
# )
# print(ab)

a=np.array([(1,2,3),(5,4,3)],complex) 
#print(a)


#arange(<from>,<to>,<step>,[<data_type>])
b=np.arange(8,32,4,float)
#print(b)
# 


#np.zeros(dimention, data_type) and np.ones(dimention, data_type): Generate multi-dimensional arrays filled entirely with zeros or ones,
zeroes = np.zeros((2, 3), dtype=np.int16)
#print(zeroes)

#np.linspace(<first>,<last>,<size>): Generates an array of evenly spaced numerical values across a strictly defined interval.
a_linspace = np.linspace(-1, 1, 6)
#print("Linspace Array:", a_linspace)

#np.logspace(<first>,<last>,<size>): Generates an array of values spaced evenly on a logarithmic scale.
a_logspace = np.logspace(10, 0, 6)
#print("Logspace Array:", a_logspace)




A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
# print("Element-wise product:\n", A * B)
# print("Matrix product (dot):\n", A.dot(B))

a = np.array( [20,30,40,50] )
b = np.arange( 4 )
# print(b)
c = a + b
# print(c)
# print(b**2)

# Aggregation and reshaping. columns (axis=0) rows -> axis =1
unshape_array = np.arange(12)
# print(unshape_array)
shape_array= unshape_array.reshape(3, 4)
#print("\nReshaped 3x4 Array:\n", shape_array)
# print("Sum of each column (axis=0):", shape_array.sum(axis=0))
# print("Cumulative sum of each row (axis=1):\n", shape_array.cumsum(axis=1))

# Apply along axis
def custom_mean(arr):
    return np.mean(arr)
# #print("Mean applied along axis 0:", np.apply_along_axis(custom_mean, axis=0, arr=shape_array))

# Transpose and Flatten
# print("Transposed:\n", shape_array.T)
# print("Flattened (ravel):", shape_array.ravel())

print("--- 1D ARRAY SLICING ---")
a = np.arange(10, 16)
# print("Original 1D array:", a)
# print("a[1:5] (index 1 to 4):", a[1:5])
# print("a[::2] (every 2nd element):", a[::2])
# print("a[:5:2] (up to index 4, step 2):", a[:5:2])
# print("a[:5:] (up to index 4):", a[:5:])

print("\n--- 2D ARRAY SLICING ---")
A = np.arange(10, 19).reshape((3, 3))
# print("Original 2D array:\n", A)
# print("A[0,:] (First row):", A[0,:])
# print("A[:,0] (First column):", A[:,0])
# print("A[0:2, 0:2] A[rowstart:rowend, colstart:colend] (Top-left 2x2 sub-matrix):\n", A[0:2, 0:2])
# print("A[[0,2], 0:2]  (Rows 0 and 2, first two columns):\n", A[[0,2], 0:2])


print("\n--- 3. FILE I/O ---")
# Creating a dummy array and saving it
data_to_save = np.random.random((2, 2))
np.save('saved_data.npy', data_to_save)
loaded_data = np.load('saved_data.npy')
print("Data loaded from binary file:\n", loaded_data)


# Writing a dummy CSV and loading it
csv_content = "id,value1,value2\n1,123,1.4\n2,110,0.5"
with open("book_dummy.csv", "w") as f:
    f.write(csv_content)


tabular_data = np.genfromtxt('book_dummy.csv', delimiter=',', names=True)
print("Data loaded from CSV:", tabular_data)

# Cleanup local dummy files
# os.remove('saved_data.npy')
# os.remove('book_dummy.csv')


print("Opening Figure 1: Basic Line Plot... (Close window to continue)")
t = np.arange(0, 2.5, 0.1)
y1 = np.sin(math.pi * t)
y2 = np.sin(math.pi * t + math.pi/2)
plt.figure(figsize=(6, 4))
plt.title("Line Styles & Markers Combination")
plt.plot(t, y1, 'b-', label='Sine')
plt.plot(t, y2, 'g^', label='Cosine (Shifted)')
plt.axis([0, 2.5, -1.2, 1.2])
plt.legend()
# plt.show()


print("Opening Figure 2: Subplots... (Close window to continue)")
plt.figure(figsize=(8, 4))
plt.subplot(121) # 1 row, 2 cols, plot 1
plt.plot(t, y1, 'b-.')
plt.title("Plot 1")
plt.subplot(122) # 1 row, 2 cols, plot 2
plt.plot(t, y2, 'r--')
plt.title("Plot 2")
plt.show()