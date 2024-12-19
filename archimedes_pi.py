from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

def archimedes_pi(n_terms):
    getcontext().prec = 100

    side_length = Decimal(2).sqrt()
    sides = Decimal(6)
    pi = sides * side_length / Decimal(2)

    for i in range(n_terms):
        side_length = (Decimal(2) - (Decimal(4) - side_length**Decimal(2)).sqrt()).sqrt()
        sides *= Decimal(2)
        pi = sides * side_length / Decimal(2)

    return pi





def graph():
    x_points = [2, 3, 4, 5, 6, 8, 10, 12, 14, 15, 17, 18, 19]
    y_values = [
        1.18307924270629883, 2.46275823474949283, 6.32471976336078912, 16.40521284313748254,
        33.05881731922903871, 69.29471211182738307, 211.09296083546569762, 722.05848982638191949,
        2263.93587102925617436, 4372.13218393259688452, 8617.49377694713375756,
        17992.43048513184719873, 36623.71631453842904884
    ]

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_values, marker='o', linestyle='-', color='b', label='Время вычисления')

    # plt.yscale('log')
    plt.xlabel('Количество итераций', fontsize=12)
    plt.ylabel('Время вычисления (с)', fontsize=12)
    plt.title('График зависимости времени вычисления от количества знаков', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    plt.savefig("graph/archimedes_pi.png")
    plt.close()


graph()

