start = int(input("Введите начало диапазона: "))
finish = int(input("Введите конец диапазона: "))
n = start and finish % 2 == 0 

if start == finish and n is True:
    print(0)
else: 
    start == finish and n is False
    print(start)

if start < finish:
    for num in range(start + 1, finish + 1, 2):
        print(num)
else:
    start > finish 
    for num in range (finish, start + 1, 2):
        print(num)