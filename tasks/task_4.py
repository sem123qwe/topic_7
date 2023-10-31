num = 0
n = 1
user_input = int(input("Введите число:"))
while n <= user_input:
    num += n
    n += 1
    print("Сумма всех чисел от", 1, "до", user_input, "равна:", num)

