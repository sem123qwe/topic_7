rows: int = int(input("Введите целое положительное число: "))
for n in range (1, rows + 1):
    for _ in range (n):
        print(n, end=" ")
    print()

# ----------------------

rows: int = int(input("Введите целое положительное число: "))
num: int = 1
while num <= rows:
    numbers: int = 0
    while numbers < num:
        print(num, end=" ")
        numbers += 1
            
    print()
    
    num += 1
