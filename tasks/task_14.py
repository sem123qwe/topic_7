rows: int = int(input("Введите целое положительное число: "))
for num in range(rows, 0, -1):
    spaces: int = rows - num
    for _ in range(spaces):
        print(" ", end="")

    stars: int = 2 * num - 1
    for stars in range(stars):
        print("*", end="")

    print()

for num in range(2, rows + 1):
    spaces: int = rows - num
    for _ in range(spaces):
        print(" ", end="")

    stars: int = 2 * num - 1
    for stars in range(stars):
        print("*", end="")

    print()

print()
# ----------------------------------------------------

# rows: int = int(input("Введите целое положительное число: "))
num: int = rows
while num > 0:
    spaces: int = rows - num
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars: int = 2 * num - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    num -= 1

num: int = 2
while num <= rows:
    spaces: int = rows - num
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars: int = 2 * num - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    num += 1
