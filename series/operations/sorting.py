import pandas as pd


#based on values

# obj1 = pd.Series([58,25,67,45,86,93,75])
# print(obj1.sort_values())

#based on decending values

# obj2 = pd.Series([58,25,67,45,86,93,75])
# print(obj2.sort_values(ascending=False))

#based on index

obj3 = pd.Series([58,25,67,45,86,93,75])
print(obj3.sort_index(ascending=False))

