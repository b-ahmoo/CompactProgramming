import pandas as pd
import numpy as np
from pandas import *
import matplotlib.pyplot as plt

print("---------TASK1-------------")
df = pd.read_csv('Cars93_missing.csv')
print(df.head())

print("---------TASK2-------------")
objectdata = {'color' : 
['blue','green','yellow'],
'object' : ['ball','pen','pencil'],
'price' : [1.2,1.0,0.6]

}

print("converting objectdata into dataframe...")
dframe = pd.DataFrame(objectdata)
print(dframe)

new_object_series = pd.Series(['ID-001', 'ID-002', 'ID-003'])

print("setting new_object_series as the index of dframe using direct assignment...")
dframe.index = new_object_series
print("After assignment of new index = ", dframe)

print("setting new_object_series as the index of dframe using set_index()...")
dframe.set_index(new_object_series, inplace=True)
print("After assignment of new index = ", dframe)



print("---------TASK3-------------")

objectdata = {'color' : 
['blue','green','yellow'],
'object' : ['ball','pen','pencil'],
'price' : [2,1,4]

}
dframe = pd.DataFrame(objectdata)
print("identifying prices < 2 ... ")
print(dframe['price'] < 2)
dframe.loc[dframe['price']<2, 'price'] = 3
print("Updating price where price is < 1 using .loc[] function... ")
print(dframe)


print("---------TASK3-------------")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [45, np.nan, 92, np.nan],
    'Status': ['Pass', 'Fail', np.nan, 'Fail']
}
df = pd.DataFrame(data)
print("Getting names of columns...")
col_names = df.columns.tolist()
print("Column names = ", col_names)

print("Calculating sum of missing values...")
missing_values = df.isna().sum()
print("Sum of missing values = ", missing_values)

print("---------TASK4-------------")

data = {
    'Name': ['Alice', 'Zharlie', 'David', 'Bob'],
    'Score': [45, 50, 92, 100],
    'ID': ['I01', 'I02','I03','I04']
    
}
df = pd.DataFrame(data)
print(df)
cols = list(df.columns)


def exchange_cols(df, col1, col2):
    cols = list(df.columns)

    index1 = cols.index(col1)
    index2 = cols.index(col2)

    # Swap index positions of columns in the list
    cols[index2], cols[index1] = cols[index1], cols[index2]
    return df[cols]

print("Switching columns...")
switched = exchange_cols(df, 'Name', 'ID')
print(switched)
print("Sorting column by Name...")
sorted = switched.sort_values(by= 'Name')
print(sorted)


print("-----TASK6---------")
df = pd.read_csv('Cars93_missing.csv')

lowerbound = df['Price'].quantile(0.05)
upperbound = df['Price'].quantile(0.95)

new_df = df[(df['Price'] >= lowerbound ) & (df['Price'] <= upperbound)]

print("Original row count = ",len(df))
print("Filtered row count = ", len(new_df))


print("-----TASK7---------")

df = pd.read_csv('Cars93_missing.csv')
# print("Finding number of non-null values in the df... ")
# print(df.info())
print("\nNumber of missing values in column Price:\n", df['Price'].isna().sum())
print("\nRows missing values in column Price:\n", df[df['Price'].isna()])

print("Finding mean of Price column...")
avg = df['Price'].mean()
print(avg)
print("Replacing missing values with average...")
df['Price'] = df['Price'].fillna(avg)
print("\nNumber of missing values in column Price after replacement:\n", df['Price'].isna().sum())


print("-----TASK8---------")
my_dict1 = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
my_dict2 = {1: ['A', 'B'], 2: ['C', 'D'], 3: ['E', 'F']}
df1= pd.DataFrame(my_dict1)
df2= pd.DataFrame(my_dict2)
print("Vertical Merge = ")
print(pd.concat([df1,df2],ignore_index=True))

print("Horizontal merge = \n",pd.concat([df1, df2], axis=1) )

print("Appending col 2 in df2 as a new column in df1 ...")
df1['4'] = df2[1]
df1['5'] = df2[2]
df1['6'] = df2[3]
print(df1)


df_combined = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", df_combined)



print("-----TASK9---------")
df = pd.read_csv('Cars93_missing.csv')
df['Type'].hist(bins=5, edgecolor = 'black')
plt.title('Distribution of Types')
plt.xlabel('Type')
plt.ylabel('Frequency')
plt.show()

print("-----TASK10---------")
df = pd.read_csv('Cars93_missing.csv')
cols = df[['Price', 'Max.Price']]
full_matrix = cols.corr()
print(full_matrix)










