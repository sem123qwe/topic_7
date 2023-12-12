rows: int = int(input("Введите целое положительное число: "))
for num in range(1, rows + 1):
    spaces: int = rows - num
    for _ in range(spaces):
        print(" ", end="")

    stars: int = 2 * num - 1
    for stars in range(stars):
        print("*", end="")

    print()

for num in range(rows - 1, 0, -1):
    spaces = rows - num
    for _ in range(spaces):
        print(" ", end="")

    stars: int = 2 * num - 1
    for stars in range(stars):
        print("*", end="")

    print()

# ----------------------------------------------------


# rows: int = int(input("Введите целое положительное число: "))
num: int = 1
while num <= rows:
    spaces = rows - num
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    stars: int = 2 * num - 1
    while stars > 0:
        print("*", end="")
        stars -= 1

    print()

    num += 1


num: int = rows - 1
while num > 0:
    spaces = rows - num
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    stars: int = 2 * num - 1
    while stars > 0:
        print("*", end="")
        stars -= 1

    print()

    num -= 1
