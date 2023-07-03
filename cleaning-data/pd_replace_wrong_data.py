
import pandas as pd

# Fixing Wrong Data
'''
Wrong data does not have to be "empty cells" or "wrong format", 
it can just be wrong, like if someone registered "199" instead of "1.99".
'''

# Example 1: Replacing Values
# This will be a good option when we have a small amount of data.
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
df.loc[2, 'Duration'] = 45  # Replace the wrong value with 45.


# Example 2: Replacing Values
# This will be a good option when we have a large amount of data.
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120  # Replace the wrong value with 120.


# Example 3: Removing Rows
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace=True)  # Remove the row with the wrong value.
