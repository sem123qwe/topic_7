user_input: int = int(input("Введите число:"))

if user_input < 0:
    print("Факториал определен только для натуральных чисел.")
else:
    num: int = 1
    n: int = 1

    while n <= user_input:
        num *= n
        n += 1

    print("Факториал числа", user_input, "равен", num)
