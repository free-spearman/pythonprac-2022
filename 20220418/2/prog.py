class SquareIO:

    def inputCoeff(self, name):
        coeff_value = input(f"Input {name}:")
        return coeff_value

    def printResult(self, result):
        print(f"Solution: {result}")

def solveSquare():
    coeff_values = []
    try:
        for coeff_name in ['a','b','c']:
            coeff_values.append(float(SquareIO().inputCoeff(coeff_name)))
        a, b, c = coeff_values
    except Exception:
        SquareIO().printResult('bad... wrong number entered')
        return
    if a == 0:
        if b == 0:
            if c == 0:
                SquareIO().printResult('R')
                return
            SquareIO().printResult('no solution')
            return
        
        SquareIO().printResult((-c / b,) )
        return
    D = b ** 2 - 4 * a * c
    if D < 0:
        SquareIO().printResult('no solution')
        return    
    SquareIO().printResult(((-b - D**0.5) / 2 * a, (-b + D**0.5) / 2 * a))
    return

if __name__ == "__main__":
    solveSquare()