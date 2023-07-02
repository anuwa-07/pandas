import pandas as pd
import numpy as np

"""
What is a Series?
- Series is like a column in a Table
- One dimensional array, which can hold any data type.
"""
arr_1: np.ndarray = np.array([1, 2, 3, 4, 5])
my_var_1: pd.Series = pd.Series(arr_1)
print(my_var_1)
#
''' 
Example Output:
0    1
1    2
2    3
3    4
4    5
'''

"""
Labels
- With the index argument, you can name your own labels.
"""
arr_2: np.ndarray = np.array([1, 2, 3, 4, 5])
my_var_2: pd.Series = pd.Series(arr_2, index=['A', 'B', 'C', 'D', 'E'])
print(my_var_2)
#
'''
Example Output:
A    1
B    2
C    3
D    4
E    5
'''

# With the labels you can access an item.
print(my_var_2['C'])
'''
Example Output:
3
'''


"""
Object Type as Series Value
- You can use any object type as value in a Series.
"""
calories: dict = {
    'day1': 420,
    'day2': 380,
    'day3': 390
}
my_var_3: pd.Series = pd.Series(calories)
print(my_var_3)
#
'''
Example Output:
day1    420
day2    380
day3    390
'''

# To select only some of the items in the dictionary,
# use the index argument and specify only the items you want to include in the Series.
calories: dict = {
    'day1': 420,
    'day2': 380,
    'day3': 390
}
my_var_4: pd.Series = pd.Series(calories, index=['day1', 'day2'])
print(my_var_4)
#
'''
Example Output:
day1    420
day2    380
'''


"""
DataFrames
- A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
- Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
- Series is like a column, a DataFrame is the whole table.
"""
data: dict = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}
my_var_5: pd.DataFrame = pd.DataFrame(data)
print(my_var_5)
#
'''
Example Output:
    calories  duration
0        420        50
1        380        40
2        390        45
'''
# With using the `loc` attribute, you can return the row with the index 0.
print(my_var_5.loc[0])
#
'''
Example Output:
calories    420
duration     50
Name: 0, dtype: int64
'''
# use a list of indexes:
print(my_var_5.loc[[0, 1]])
#
'''
Example Output:
    calories  duration
0        420        50
1        380        40
'''
# You can also use the Name index, for dataframes.
data: dict = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}
my_var_6: pd.DataFrame = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(my_var_6)
#
'''
Example Output:
        calories  duration
day1        420        50
day2        380        40
day3        390        45
'''















