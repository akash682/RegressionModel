import numpy as np
import math
import matplotlib.pyplot as plt
import matrix_calcinside as mci

x_data = np.arange(0.0, 1.1, 0.1, dtype="float")
y_data = []
for x in x_data:
    y_data.append(math.sin(2*math.pi*x))
ran = np.random.normal(0, 0.3, 11)
y_data = y_data + ran

print("X:", x_data)
print("Y:", y_data)

M=9
N = len(x_data)
Lambda = math.e**(-18)

left_A = mci.left_calc(x_data, M, N)
right = mci.right_calc(x_data, y_data, M, N)
left_lambda = mci.identity_calc(Lambda, M)

left = left_A + left_lambda
left_inverse = np.linalg.inv(left)
w = np.matmul(left_inverse, right)

x_fit, y_fit = np.array(mci.test_calc(w, M))


plt.scatter(x_data, y_data)
plt.scatter(x_fit, y_fit)
plt.show()