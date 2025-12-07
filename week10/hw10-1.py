import numpy as np
import time
from scipy.linalg.blas import dgemm  

A = np.random.rand(200, 200)
B = np.random.rand(200, 200)
def matrixm(X, Y):
    n, m = X.shape
    p = Y.shape[1]
    result = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            sum_val = 0
            for k in range(m):
                sum_val += X[i, k] * Y[k, j]
            result[i, j] = sum_val
    return result
start = time.perf_counter()
C = matrixm(A, B)
end = time.perf_counter()
timem = end - start
start_scipy = time.perf_counter()
C_scipy = dgemm(alpha=1.0, a=A, b=B)
end_scipy = time.perf_counter()
time_scipy = end_scipy - start_scipy
print(f"自行實作版本執行時間: {timem:.6f} 秒")
print(f"SciPy加速版本執行時間: {time_scipy:.6f} 秒")
print("矩陣相近:", np.allclose(C, C_scipy))
