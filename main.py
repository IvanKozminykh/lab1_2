def gcd(a, b):
    """Вычисление НОД (наибольшего общего делителя) с использованием алгоритма Евклида."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Ввод чисел от пользователя
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = gcd(num1, num2)
    print(f"Наибольший общий делитель чисел {num1} и {num2}: {result}")
except ValueError:
    print("Пожалуйста, вводите только целые числа.")
