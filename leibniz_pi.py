from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

def leibniz_pi(num_terms, precision):
    getcontext().prec = precision
    pi = Decimal(0)
    for k in range(num_terms):
        pi += Decimal((-1)**k) / (2 * k + 1)
    return 4 * pi

def gparh():
    x_points = [1, 5, 10, 15, 20, 25, 30]
    y_values = [0.0, 0.0041, 0.05, 0.4, 3.9, 39.0, 450.0]

    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_values, marker='o', linestyle='-', color='b', label='Время вычисления')

    plt.yscale('log')
    plt.xlabel('Количество знаков точности π', fontsize=12)
    plt.ylabel('Затраченное время (с)', fontsize=12)
    plt.title('График зависимости времени вычисления от количества знаков', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    # Показать график
    plt.savefig("graph/leibniz_pi.png")
    plt.close()

gparh()

