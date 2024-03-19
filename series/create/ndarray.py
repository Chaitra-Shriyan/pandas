import pandas as pd
import numpy as np

# nd = np.arange(5,28,5)
# print(nd)
#
# obj1 = pd.Series(nd)
# print(obj1)

#wap
#5 elements in range(24 to 64)

# obj2 = pd.Series(np.linspace(24,64,5))
# print(obj2)

#tiling list[3,5] tiwce


obj3 = pd.Series(np.tile([3,5],2))
print(obj3)