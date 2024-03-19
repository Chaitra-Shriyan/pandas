import pandas as pd



obj1 = pd.Series([9,5,8,2,1,3])
print(obj1)

obj2 = obj1.reindex([1,3,2,0,4])
print(obj2)
