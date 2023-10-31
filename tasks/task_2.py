num: int = int(input("Введите число: "))
print("Таблица умножения для числа", num, "с помощью цикла for:")
for n in range(11):
    n *= num
    print(n)

n: int = 1
num: int = int(input("Введите число: "))
print("Таблица умножения для числа", num, "с помощью цикла whill:")
while n <= 10:
    resualt = n * num
    n += 1
    print(resualt)
