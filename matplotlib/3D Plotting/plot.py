# # Rnl(r) = sqrt([(2Z/na_0)^3][(n-l-1)!/2n(n+l)!])e^(-Zr/na_0)
# Z = 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
import math

a0 = 0.529 * pow(10, -10)

# Create an array of radial distances
r = np.linspace(0, 200 * a0, 1000)


def hydrogen_radial_wavefunction(n, l, r):
    # a0 = 0.529 * pow(10, -10)
    norm = math.sqrt(((2 / (n * a0)) ** 3) * (math.factorial(n - l - 1) / (2 * n * math.factorial(n + l))))
    laguerre_term = genlaguerre(n - l - 1, 2 * l + 1)(2 * r / (n * a0))
    exponential_term = np.exp(-r / (n * a0))
    return norm * laguerre_term * ((2 * r / (n * a0))) ** l * exponential_term


# Input: principal quantum number
n = int(input("Enter the principal quantum number (n): "))

# All l values for a given n
l_values = [i for i in range(0, n)]

# Number of Plots Required
num_plots = len(l_values)

figs = [None] * num_plots
axes = [None] * num_plots


# Create the plots and store the figures and axes in the arrays
for i in range(num_plots):
    figs[i], axes[i] = plt.subplots()

print(figs, axes)
for i, l in enumerate(l_values):
    wavefunction = hydrogen_radial_wavefunction(n, l, r)
    axes[i].plot(r,wavefunction)
    axes[i].set_title(f"Radial Wave Function n={n}, l={l}")
    axes[i].set_xlabel("Radial distance (r)")
    axes[i].set_ylabel("Radial Wave Funciton")

#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(r, np.zeros_like(r), wavefunction, label=f'R{str(n)}')
# ax.set_xlabel('r')
# ax.set_ylabel('Real')
# ax.set_zlabel('Imaginary')
# ax.set_title(f'Radial Wave Function for n = {n}')

plt.tight_layout()
plt.show()
