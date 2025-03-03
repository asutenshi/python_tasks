import numpy as np
import matplotlib.pyplot as plt

# Функция
def f(x):
    return 2 * x

# Параметры
a = 1  # точка a
L = f(a)  # предел
epsilon = 0.1  # заданное значение ε
delta = epsilon / 2  # δ, найденное из |2x - 2| < ε

# Область определения
x = np.linspace(0.5, 1.5, 500)
y = f(x)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = 2x", color="blue")

# Область вокруг предела L
plt.axhline(L + epsilon, color="red", linestyle="--", label="L + ε")
plt.axhline(L - epsilon, color="red", linestyle="--", label="L - ε")

# Область вокруг точки a
plt.axvline(a + delta, color="green", linestyle="--", label="a + δ")
plt.axvline(a - delta, color="green", linestyle="--", label="a - δ")

# Точки на графике
plt.scatter([a], [L], color="black", zorder=5, label="Точка (a, L)")

# Настройки графика
plt.title("Графическая иллюстрация определения предела")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(L, color="black", linestyle="-", linewidth=0.8, label="L")
plt.axvline(a, color="black", linestyle="--", linewidth=0.8, label="a")
plt.legend()
plt.grid()
plt.show()
