import math


def convert_precision(tolerance):
    """
      Функция convert_precision принимает значение точности вычислений (tolerance)
      и возвращает порядок этого значения.
      Например, для значения 1e-6 функция вернет 6.
      """
    try:
        tolerance = float(tolerance)
    except ValueError:
        print('Значение точности передано в неправильном формате')
        print('Взято значение по умолчанию 1e-6')
        return 6

    if tolerance >= 1 or tolerance < 0:
        print('Значение точности передано в неправильном формате')
        print('Взято значение по умолчанию 1e-6')
        return 6
    elif tolerance == 0:
        return 0

    return int(math.log10(1 / tolerance))


def calculate(num1, num2, operation, precision=6):
    """
      Функция calculate выполняет арифметическое действие на двух числах с заданной точностью вычислений.

      Параметры:
      - num1 (float): Первое число.
      - num2 (float): Второе число.
      - operation (str): Тип арифметической операции: '+', '-', '*' или '/'.
      - tolerance (float): Точность вычислений (по умолчанию 1e-6).

      Возвращает:
      - result (float): Результат арифметической операции с заданной точностью.
      """
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError('Необходимо ввести числа!')

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # Проверка деления на ноль
        try:
            result = num1 / num2
        except ZeroDivisionError:
            raise ZeroDivisionError('Деление на ноль!')
    else:
        raise ValueError('Необходимо выбрать операцию из списка!')

    rounded_result = round(result, precision)
    return rounded_result


def main():
    """
    Функция main запрашивает у пользователя два числа и операцию, а затем вызывает функцию calculate для вычисления результата.
    """
    # Ввод чисел и операции
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /): ")

    tolerance = input("Введите точность (например: 1е-6, 0.001): ")

    # Вызов функции calculate для вычисления результата
    result = calculate(num1, num2, operation, convert_precision(tolerance))

    # Вывод результата
    if result is not None:
        print("Результат: ", result)


# Вызов функции main
if __name__ == '__main__':
    main()
