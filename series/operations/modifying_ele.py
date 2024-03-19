import pandas as pd

#by assignment

# obj1 = pd.Series([10,23,67,42,90])
# obj1[3]=100
# print(obj1)

#by slicing

obj2 = pd.Series([10,23,67,42,90])
obj2[0::2]=100
print(obj2)