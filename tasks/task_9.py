numbers: list = [
    "105", "42", "98", "120", "84", "80", "110", "119", "130", "99"
]

print("Числа, кратные 5 или 7 и больше 100:", end=" ")
for m in range(0, len(numbers)):
    num: int = int(numbers[m])
    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        print(num, end=" ")
        m += 1
print()

# ---------------------------

print("Числа, кратные 5 или 7 и больше 100:", end=" ")
for num in numbers:
    num: int = int(num)
    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        print(num, end=" ")
print()




# rows = int(input("Введите целое положительное число: "))
# num = 1
# while num <= rows:
#     spaces = rows - num
#     while spaces > 0:
#         print(" ", end=" ")
#         spaces -= 1
    

#     stars = 1
#     while stars + 1 <= num * 2:
#         print("*", end=" ")
#         stars += 1

#     print()
        
#     num += 1