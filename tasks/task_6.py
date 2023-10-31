user_input: int = abs(int(input("Введите целое число: ")))

counter: int = 0

while user_input > 1:  
    user_input //= 10
    counter += 1

print("Количество цифр в числе:", counter)
