def solveSquare(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    else:
        x_1 = (-b + D**0.5) / (2 * a)
        x_2 = (-b - D**0.5) / (2 * a)
        return (min(x_1, x_2), max(x_1, x_2))

print( solveSquare(-2, 4, 2))