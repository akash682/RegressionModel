import numpy as np

def left_calc(x_data, M, N):
    S = np.zeros((M + 1, M + 1))

    for j in range(0, M + 1):
        for i in range(0, M + 1):
            sum = 0
            for r in range(0, N):
                sum += x_data[r] ** (i + j)
            S[i, j] = sum

    return S

def right_calc(x_data, y_data,  M, N):
    S = np.zeros((M+1, 1))

    for i in range(0, M+1):
        sum = 0
        for r in range(0, N):
            sum += y_data[r]*(x_data[r]**(i))
        S[i, 0] = sum

    return S

def test_calc(w, M):
    x_fit = np.arange(0, 1, 0.01)
    y_fit = []
    for i in range(0, len(x_fit)):
        y = 0
        for j in range(0, M + 1):
            y += w[j] * x_fit[i] ** (j)
        y_fit.extend(y)
    return x_fit, y_fit

def identity_calc(Lambda, M):
    R = np.zeros((M+1, M+1))
    for i in range(0, M+1):
        for j in range(0, M+1):
            if i==j:
                R[i,j] = Lambda

    return R