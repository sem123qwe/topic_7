numbers: list = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

m: int = 0
forest: list = list()


for m in range(len(numbers)):
    
    num: int = int(numbers[m])
    
    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        forest.append(num)
        m += 1
    
print("Числа, кратные 5 или 7 и больше 100: ", forest)
