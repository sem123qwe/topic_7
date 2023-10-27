user_input_start = int(input("Введите начало диапазона: "))
user_input_finish = int(input("Введите конец диапазона: "))
for num in range(user_input_start, user_input_finish + 1, 2):
    print(num)
    
