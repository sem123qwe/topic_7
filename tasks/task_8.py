start = int(input("Введите начало диапазона: "))
finish = int(input("Введите конец диапазона: "))

n = start and finish % 2 == 0

if start == finish and n is True:
    print(0)
else:
    if start == finish and n is False:
        print(start)

if start < finish:
    for num in range(start + 1, finish + 1, 2):
        print(num)
else:
    if start > finish:
        for num in range(finish, start + 1, 2):
            print(num)

# ----------------------------

start: int = int(input("Введите начало диапазона: "))
finish: int = int(input("Введите конец диапазона: "))

if start > finish:
    start, finish = finish, start

for num in range(start, finish + 1):
    if num % 2 == 0:
        print(num)
    elif start == finish:
        if start % 2 != 0:
            print(0)
        else:
            print(start)

# ----------------------------

start: int = int(input("Введите начало диапазона: "))
finish: int = int(input("Введите конец диапазона: "))

if start > finish:
    start, finish = finish, start

for num in range(start, finish + 1):
    if num % 2 == 0:
        print(num)
    elif start == finish:
        print(0)
