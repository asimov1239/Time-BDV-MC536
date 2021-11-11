import pandas as pd

series = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print(series.loc[['A', 'B']])