import numpy as np
import matplotlib.pyplot as plt

# Definir la función objetivo
def f(x):
    return -35 / 961 * (x - 31)**2 + 40

# Generar datos para la gráfica
x_values = np.linspace(0, 63, 500)  # Rango de x, de 0 a 63 (cromosomas de 6 bits)
y_values = f(x_values)  # Calcular f(x) para cada valor de x

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$f(x) = -\frac{35}{961}(x - 31)^2 + 40$', color='b')
plt.title("Gráfica de la función objetivo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axvline(x=31, color='r', linestyle='--', label="Máximo en x = 31")  # Mostrar el máximo en x = 31
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
