
import pandas as pd
import numpy as np

"""
    Process CSV file with Pandas
"""
# Configure Pandas, to max rows to display
pd.options.display.max_rows = 5
#
# Read CSV file
df: pd.DataFrame = pd.read_csv('./test-data/data-set01.csv')
print("Show the values from CSV file")
print("Shape: ", df.shape)
print(df.info())
print(df)


"""
    Process JSON file with Pandas
"""
# Configure Pandas, to max rows to display
pd.options.display.max_rows = 7
#
# Read JSON file
df: pd.DataFrame = pd.read_json('./test-data/data-set02.json')
print("Show the values from JSON file")
print("Shape: ", df.shape)
print(df.info())
print(df)
