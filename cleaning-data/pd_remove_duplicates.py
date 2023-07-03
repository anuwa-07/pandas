
import pandas as pd

# Removing Duplicates
'''
Duplicate rows are rows that have been registered more than one time.
'''

# To Identify Duplicates
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
print(df.duplicated())  # Returns a Boolean value for each row, True if a row is a duplicate, otherwise False.

# To Remove Duplicates
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)  # Remove all duplicates.
