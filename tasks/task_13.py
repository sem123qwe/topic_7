rows: int = int(input("Введите целое положительное число: "))
num: int = 0
for n in range (rows):
    for _ in range (n + 1):
        num += 1
        print(num, end=" ")
    print()

# --------------------------------

rows = int(input("Введите целое положительное число: "))
num = 1
counter = 1
while num <= rows:
    spaces = num - rows
    while spaces > 0:
        print(" ", end=" ")
        spaces -= 1
    
    stars = 1
    while stars <= num:
        print(counter, end=" ")
        stars += 1
        counter += 1

    print()
    
    num += 1
