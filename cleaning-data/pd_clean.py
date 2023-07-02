import pandas as pd

"""
    Cleaning data with Pandas
    - Data cleaning means fixing bad data in your data set.
    - Bad data could be:
        - Empty cells
        - Data in wrong format
        - Wrong data
        - Duplicates
"""

# Cleaning Empty Cells
# --------------------
# Remove Rows
'''
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''
df: pd.DataFrame = pd.read_csv('./test-data/data.csv')
# `dropna()` method returns a new DataFrame, and will not change the original.
# Use `inplace=True` to change the original
new_df: pd.DataFrame = df.dropna()
print(new_df.to_string())

# Replace Empty Values
'''
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The `fillna()` method allows us to replace empty cells with a value
'''
df: pd.DataFrame = pd.read_csv('./test-data/data.csv')
# Replace all empty cells with 130
df.fillna(130, inplace=True)  # inplace=True will change the original

# If you want to replace all empty values specific `column`.
df['Calories'].fillna(130, inplace=True)  # inplace=True will change the original


# Replace Using Mean, Median, or Mode
# - This is more accurate than using a single value

# Mean
'''
Mean = the average value (the sum of all values divided by number of values).
'''
df: pd.DataFrame = pd.read_csv('./test-data/data.csv')
x: float = df['Calories'].mean()  # get the mean value
df['Calories'].fillna(x, inplace=True)  # replace all empty values in 'Calories' column with the mean value

# Median
'''
Median = the value in the middle, after you have sorted all values ascending.
'''
df: pd.DataFrame = pd.read_csv('./test-data/data.csv')
x: float = df['Calories'].median()  # get the median value
df['Calories'].fillna(x, inplace=True)  # replace all empty values in 'Calories' column with the median value

# Mode
'''
Mode = the value that appears most frequently.
'''
df: pd.DataFrame = pd.read_csv('./test-data/data.csv')
x: float = df['Calories'].mode()[0]  # get the mode value
df['Calories'].fillna(x, inplace=True)  # replace all empty values in 'Calories' column with the mode value


