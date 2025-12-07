import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return np.exp(-(x**2))

x = np.linspace(-1, 3, 1000)
I, error = integrate.quad(f, 0, 2)
plt.figure(figsize=(12, 6))
plt.plot(x, f(x), label='f(x) = exp(-x^2)', linewidth=2)
x_fill = np.linspace(0, 2, 500)
plt.fill_between(x_fill, f(x_fill), color='orange', alpha=0.4,
                 label=f"Integral area (0→2), I ≈ {I:.6f}")
plt.title("I = ∫₀² exp(-x²) dx")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.text(1.2, 0.8, f"I = {I:.6f}", fontsize=12, color='red')
plt.show()
print(f"定積分 I = ∫₀² exp(-x²) dx = {I:.6f}")
