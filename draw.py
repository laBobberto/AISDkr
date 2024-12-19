import math
import matplotlib.pyplot as plt

def archimedes_method(iterations):
    sides = 6
    radius = 1
    side_length_inscribed = radius
    points = []

    for i in range(iterations):
        side_length_inscribed = math.sqrt(2 - 2 * math.sqrt(1 - (side_length_inscribed / 2)**2))
        sides *= 2
        pi_approximation = sides * side_length_inscribed / (2 * radius)
        points.append((i + 1, pi_approximation))

    return pi_approximation, points, sides, side_length_inscribed

def plot_pi_approximations(points):
    iterations, approximations = zip(*points)
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, approximations, marker='o', label='Приближение пи')
    plt.axhline(y=math.pi, color='r', linestyle='--', label=f'Истинное значение π ({math.pi})')
    plt.title('Приближение числа π методом Архимеда')
    plt.xlabel('Итерация')
    plt.ylabel('Приближение π')
    plt.legend()
    plt.grid()
    plt.show()

def plot_polygon(sides, radius, side_length):
    angle = 2 * math.pi / sides
    vertices = [
        (math.cos(i * angle) * radius, math.sin(i * angle) * radius) for i in range(sides)
    ]

    vertices.append(vertices[0])
    x, y = zip(*vertices)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o', label=f'{sides}-угольник')
    circle = plt.Circle((0, 0), radius, color='r', fill=False, linestyle='--', label='Окружность')
    plt.gca().add_artist(circle)
    plt.title(f'Вписанный {sides}-угольник')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    iterations = 5
    pi_value, points, sides, side_length = archimedes_method(iterations)
    print(f"Приближенное значение числа пи после {iterations} итераций: {pi_value}")
    plot_pi_approximations(points)
    plot_polygon(sides, 1, side_length)
