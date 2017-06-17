import numpy as np

b = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(b)

c = b[np.where(b>3)]
print(c)
