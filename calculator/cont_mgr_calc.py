from calculator.calculator import calculate


class BatchCalculatorContextManager:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with BatchCalculatorContextManager('calc.txt') as f:
        for line in f:
            a, op, b = line.split()
            result = calculate(int(a), int(b), op)
            print(f"Result of {a} {op} {b} = {result}")
