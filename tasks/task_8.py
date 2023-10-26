user_input_start = int(input("Введите начало диапазона: "))
user_input_finish = int(input("Введите конец диапазона: "))
if user_input_start == (user_input_finish % 2 == 0):
    print(user_input_start)
elif user_input_start == user_input_finish:
    print(0)
    
