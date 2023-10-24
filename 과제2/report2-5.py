def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("소수 검색 할 정수를 입력하시오:"))
if is_prime(num):
    print("소수인가요?:true:")
else:
    print("소수인가요?:flase")