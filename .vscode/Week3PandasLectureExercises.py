import pandas as pd
import numpy as np
from pandas import *

s = pd.Series([12,-4,7,9])
print(s)

s = pd.Series([12,-4,7,9],index=['a','b','c','d'])
print(s)
print(s.values,s.index)

print("s['a'] = ",s['a'])
t = pd.Series([10,20,30,40])  
print("t[0] = ",t[0])

s = pd.Series([12,-4,7,9], 
index=['a','b','c','d'])
print("s[0:2] = ", s[0:2])
print("s[2:] = ", s[2:])

print("s[s > 8] = ",s[s > 8])

s = pd.Series([12,-4,7,9], 
index=['a','b','c','d'])
print(s / 2)
print("np.log(s) = ",np.log(s))


serd = pd.Series([1,0,2,1,2,3], 
index=['white','white','blue','green','green','yellow'])
print("serd.unique() = ",serd.unique())
print("serd.value_counts() = ",serd.value_counts())
print("serd.isin([0,3]) = ",serd.isin([0,3]))


mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
print("myseries = ",myseries)


colors = ['red','yellow','orange','blue','green']
mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries1 = pd.Series(mydict,index=colors)
print("pd.Series(mydict,index=colors) = ",myseries1)


print("-------pandas Data Structures: DataFrame-------------")

data = {'color' : 
['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]

}

frame = pd.DataFrame(data)
print("frame = ",frame)
frame2 = pd.DataFrame(data, columns=['object','price'])
print("frame2 = ",frame2)

print("-----2D array as input into DF--------")
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print("pd.DataFrame(my_2darray) = ")
print(pd.DataFrame(my_2darray))


print("---Take a dictionary as input to your DataFrame---")
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print("my_dict = ")
print(my_dict)
print("pd.DataFrame(my_dict) = ")
print(pd.DataFrame(my_dict))

my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print("my_df = ")
print(my_df)
print("pd.DataFrame(my_df)")
print(pd.DataFrame(my_df))

print("--- Take a Series as input to your DataFrame---")
my_series = pd.Series({"Belgium":"Brussels", "India":"New Delhi", "United Kingdom":"London", "United States":"Washington"})
print(my_series)
print(pd.DataFrame(my_series))
