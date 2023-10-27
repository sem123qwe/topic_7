user_input = int(input("Введите число:"))

if user_input < 0:
    print("Факториал определен только для натуральных чисел.")
elif user_input == 0:  # TODO: Это можно улучшить
    print("Факториал числа 0 равен 1")
else:
    num = 1
    n = 1

    while n <= user_input:
        num *= n
        n += 1

    print("Факториал числа", user_input, "равен", num)
