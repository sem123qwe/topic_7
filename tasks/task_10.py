# user_input: int = abs(int(input("Введите целое число: ")))

# counter: set = set()

# while user_input > 1:
#     user_input //= 10
#     counter.add(user_input)

# print("Количество цифр в числе:", counter)

# user_input_2: int = abs(int(input("Введите целое число: ")))

# while user_input > 1:
#     user_input //= 10
#     counter.add(user_input_2)

# print("Количество цифр в числе:", sum(counter))


start: int = abs(int(input("Введите целое число: ")))
finish: int = abs(int(input("Введите целое число: ")))

if start == finish or (start < 0 or finish < 0):
    print("Некорректный диапазон")
else:

    if start > finish:
        start, finish == finish, start

    for num in range(start, finish + 1):
        count = len(str(num))

        num_copy = num
        summa = 0
        while num_copy > 0:
            last_diget = (num_copy % 10) ** count
            summa += last_diget
            num_copy //= 10

        if num == summa:
            print(num, end=" ")

# 153 --> 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
