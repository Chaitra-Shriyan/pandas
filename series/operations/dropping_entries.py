import pandas as pd



obj1 = pd.Series([9,5,8,2,1,3])
obj1 = obj1.drop([2,3])
print(obj1)
