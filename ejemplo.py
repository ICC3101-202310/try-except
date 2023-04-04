class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    
class CalculatorNoStatus:
    @classmethod
    def sum(cls, x, y):
        return x + y


calc = Calculator(1, 2)
print(calc.sum())
calc.a = 5
print(calc.sum())

print(CalculatorNoStatus.sum(1, 2))