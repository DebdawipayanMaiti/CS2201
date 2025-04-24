
import numpy as np
import scipy.integrate as spi

N = 10
xs, h = np.linspace(0, 1, N, endpoint=False, retstep=True)
ys = xs**10
irect = h * np.sum(ys)
print(f"Rectangular = {irect:.5f}")
print(f"Actual = {1/11:.5f}")

xs, h = np.linspace(0, 1, N, endpoint=True, retstep=True)
ys = xs**10
itrap = h * (0.5 * (ys[0] + ys[-1]) + np.sum(ys[1:-1]))
print(f"Trapezoidal = {itrap:.5f}")

itrap1 = spi.trapz(ys, xs)
print(f"Trapezoidal scipy = {itrap1:.6f}")

itrap2 = np.trapz(ys, xs)
print(f"Trapezoidal numpy = {itrap2:.6f}")

xs, h = np.linspace(0, 1, N + 1, endpoint=True, retstep=True)
ys = xs**10
isimp = (h / 3) * (ys[0] + ys[-1] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-1:2]))
print(f"Simp = {isimp:.5f}")

actual = 1 / 11
print(f"Actual = {actual:.6f}")
print(f"Error simp = {abs(isimp - actual):.5f}")
print(f"Error trap = {abs(itrap - actual):.5f}")

isimp1 = spi.simps(ys, xs)
print(f"Simp scipy = {isimp1:.6f}")
