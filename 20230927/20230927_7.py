'''2023.9.27
석홍신(202195056)
 설명 :  반복문으로 펙토리얼 구하기.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("숫자를 입력하십시오: "))
result = factorial(num)
print(f"!: {result}")
