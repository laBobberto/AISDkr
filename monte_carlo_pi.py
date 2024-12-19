import random
import time
import matplotlib.pyplot as plt

# from tqdm import tqdm
def monte_carlo_pi(num_points):
    inside_circle = 0

    for _ in tqdm(range(num_points)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi = 4 * inside_circle / num_points
    return pi


def gparh():
    x_points = [1, 2, 3, 4, 5, 6, 7, 8]
    y_values = [0.03, 0.007, 0.09, 0.7, 7, 70.5, 715.0, 7200.0]

    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_values, marker='o', linestyle='-', color='b', label='Время выполнения')


    plt.yscale('log')
    plt.xlabel('Вычислено знаков', fontsize=12)
    plt.ylabel('Затраченное время (с)', fontsize=12)
    plt.title('График зависимости времени выполнения от количества знаков', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()


    plt.savefig("graph/monte_carlo_pi.png")
    plt.close()

