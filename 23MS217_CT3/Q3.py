# Importing the libraries
import numpy as np
import math
from scipy.integrate import trapezoid, simpson

# Function definition
def f(x):
    return 1/(1+x**2)

# Interval and number of subintervals
a, b = 0, 1
N = 10
xs, h = np.linspace(a, b, N + 1, retstep=True)
ys = f(xs)

# Actual value of the integral
actual = 0.78 
# Rectangular Rule (Left endpoint)
I_rect = h * np.sum(f(xs[:-1]))
diff_rect = abs(I_rect - actual)

# Trapezoidal Rule (Manual)
I_trap = h * (0.5 * ys[0] + np.sum(ys[1:-1]) + 0.5 * ys[-1])
diff_trap = abs(I_trap - actual)

# Simpson’s Rule (Manual)
if N % 2 == 0:
    I_simp = h / 3 * (ys[0] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-1:2]) + ys[-1])
    diff_simp = abs(I_simp - actual)
else:
    I_simp = None
    diff_simp = None

# Trapezoidal Rule (SciPy)
I_trap_scipy = trapezoid(ys, xs)
diff_trap_scipy = abs(I_trap_scipy - actual)

# Simpson’s Rule (SciPy)
I_simp_scipy = simpson(ys, xs)
diff_simp_scipy = abs(I_simp_scipy - actual)

# Print results
print("Value of integration by scipy trapezoid: ",I_trap_scipy)
print("Value of integration by scipy simpson: ",I_simp_scipy)
print("Value of integration by manual trapezoid: ",I_trap)
print("Value of integration by manual simpson: ",I_simp)
print("Value of integration by manual rectangular: ",I_rect)
print("Difference using Rectangular Rule:     ", diff_rect)
print("Difference using Trapezoidal Rule:     ", diff_trap)
print("Difference using Simpson's Rule:       ", diff_simp)
print("Difference using Scipy Trapezoidal:    ", diff_trap_scipy)
print("Difference using Scipy Simpson's Rule: ", diff_simp_scipy)
print(np.arctan(1) - np.arctan(0))
