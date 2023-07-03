
import pandas as pd

# Cleaning Data of Wrong Format
'''
    For cleaning data of wrong format, we can use the following options:
    - remove the rows
    - convert the data into a proper format
'''

# Example 1: Convert to a Proper Format
# ------------------------------------------
df: pd.DataFrame = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Convert to a proper format if possible.
print(df.to_string())
'''
- Before:
    Date         Name  Age
0  2017-04-01  2017-04-01  42
1  2017-04-02  2017-04-02  52
2  20170403    2017-04-03  36 - Wrong format
3  2017-04-04  2017-04-04  24
4  NAN         2017-04-05  73 - Wrong format
------------------------------------------
- After:
    Date         Name  Age
0 2017-04-01  2017-04-01  42
1 2017-04-02  2017-04-02  52
2 2017-04-03  2017-04-03  36 - Converted to a proper format
3 2017-04-04  2017-04-04  24
4 NAT         2017-04-05  73 - We go a NAT value, ( Not a Time )
'''
# When we got a `NAT ( Not a Time )`, best option is to remove the row.

# Example 2: Remove Rows
# ------------------------------------------
# `dropna()` method removes rows with a NULL value, in the specified column(s).
df: pd.DataFrame = pd.read_csv('data.csv')
df.dropna(subset=['Date'], inplace=True)  # Remove rows with a NULL value, in 'Date' column.

