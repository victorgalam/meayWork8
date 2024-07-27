def mushlam_num():
    for i in range(1, 1001):
        num = i
        sumDigits = 0
        while num > 0:
            digit = num % 10
            sumDigits += digit
            num = num // 10

        if i % sumDigits == 0:
            print(i)

mushlam_num()


# num = 127
# print(num % 10)
# num = num // 10
# print(num)
# print(num % 10)
# num = num // 10
# print(num)
# print(num % 10)
# num = num // 10
# print(num)