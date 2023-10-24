for num in range(100, 1000):
    hundreds = num // 100
    tens = (num % 100) // 10
    ones = num % 10
    armstrong = hundreds**3 + tens**3 + ones**3
    if armstrong == num:
        print(num,end=" ")