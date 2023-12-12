rows = int(input("Введите целое положительное число: "))
num = 1
while num <= rows:
    spaces = rows - num
    while spaces > 0:
        print(" ", end=" ")
        spaces -= 1
    

    stars = 1
    while stars + 1 <= num * 2:
        print("*", end=" ")
        stars += 1

    print()
        
    num += 1

# -------------------------

# rows = int(input("Введите целое положительное число: "))
# for num in range(1, rows + 1):
#     spaces = rows - num
#     for _ in range(spaces):
#         print(" ", end=" ")


#     stars = 2 * num - 1
#     for stars in range(stars):
#         print("*", end=" ")

#     print()
