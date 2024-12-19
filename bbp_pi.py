from decimal import Decimal, getcontext
import matplotlib.pyplot as plt


def bbp_pi(n_terms):
    getcontext().prec = 40
    pi = Decimal(0)
    for k in range(n_terms):
        term = (Decimal(1) / Decimal(16) ** k) * (
                (Decimal(4) / (8 * k + 1)) -
                (Decimal(2) / (8 * k + 4)) -
                (Decimal(1) / (8 * k + 5)) -
                (Decimal(1) / (8 * k + 6))
        )
        pi += term
    return pi


def gparh():
    x_points = list(range(1, 33))
    y_values = [
        3.337860107421875e-05, 0.0016021728515625, 0.004813671112060547, 0.011214256286621094,
        0.023614883422851562, 0.02536606788635254, 0.037168264389038086, 0.04145312309265137,
        0.0680379867553711, 0.06390595436096191, 0.0771784782409668, 0.08441901206970215,
        0.09449219703674316, 0.10534310340881348, 0.13881921768188477, 0.12701201438903809,
        0.1403822898864746, 0.15714120864868164, 0.16830778121948242, 0.18090605735778809,
        0.1972646713256836, 0.21066641807556152, 0.22563552856445312, 0.24066400527954102,
        0.25446534156799316, 0.2716691493988037, 0.2869703769683838, 0.31116271018981934,
        0.3150014877319336, 0.33655476570129395, 0.3543374538421631, 0.36536145210266113
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_values, marker='o', linestyle='-', color='b', label='Время вычисления')

    plt.yscale('log')
    plt.xlabel('Количество знаков точности π', fontsize=12)
    plt.ylabel('Затраченное время (с)', fontsize=12)
    plt.title('График зависимости времени вычисления от количества знаков', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    plt.savefig("bbp_pi.png")
    plt.close()

gparh()