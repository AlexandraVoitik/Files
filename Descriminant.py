import math

def quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return 'No roots'
    elif d == 0:
        x = (0 - b) / 2 * a
        return f"x = {x}"
    elif d > 0:
        x1 = ((0 - b) + math.sqrt(d)) / 2 * a
        x2 = ((0 - b) - math.sqrt(d)) / 2 * a
        return f"x1 = {x1}, x2 = {x2}"

    