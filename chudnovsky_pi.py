from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

def chudnovsky_pi(n_terms):
    getcontext().prec = 40
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = L
    for i in range(1, n_terms):
        M = (K ** 3 - 16 * K) * M / i ** 3
        L += Decimal(545140134)
        X *= -262537412640768000
        K += 12
        S += M * L / X
    return C / S

def gparh():
    x_points = list(range(1, 33))
    y_values = [
        0.0009546279907226562, 0.0056188106536865234, 0.011122703552246094, 0.017966270446777344,
        0.0276486873626709, 0.027964115142822266, 0.034226417541503906, 0.03936767578125,
        0.044356346130371094, 0.05279827117919922, 0.059963226318359375, 0.061136722564697266,
        0.06822609901428223, 0.07466244697570801, 0.08160209655761719, 0.08361196517944336,
        0.09658598899841309, 0.09436225891113281, 0.11058235168457031, 0.12425088882446289,
        0.12633538246154785, 0.13007283210754395, 0.13203978538513184, 0.140183687210083,
        0.14906716346740723, 0.15706562995910645, 0.1576230525970459, 0.1615135669708252,
        0.16736197471618652, 0.1815032958984375, 0.20769119262695312, 0.18307924270629883
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_values, marker='o', linestyle='-', color='b', label='Время вычисления')

    plt.yscale('log')
    plt.xlabel('График зависимости времени вычисления от количества знаков', fontsize=12)
    plt.ylabel('Затраченное время (с)', fontsize=12)
    plt.title('График зависимости времени вычисления от количества итераций', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    plt.savefig("graph/chudnovsky_pi.png")
    plt.close()

gparh()