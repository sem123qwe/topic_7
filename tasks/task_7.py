n = 2
user_input = int(input())
while user_input > 1:
    if user_input % n == 0:
        print(n)
        user_input //= n
    else:
        n += 1
