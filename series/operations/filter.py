import pandas as pd

marks = pd.Series([58,25,67,45,86,93,75])
# print(marks>=50)
print(marks[marks>=50])
