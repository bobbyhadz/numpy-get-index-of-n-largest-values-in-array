# NumPy: Get the indices of the N largest values in an Array

import numpy as np

arr = np.array([100, 50, 20, 30, 90, 1, 5])

indices_2_largest = np.argpartition(arr, -2)[-2:]
print(indices_2_largest)  # 👉️ [4 0]

print(arr[indices_2_largest])  # 👉️ [ 90 100]