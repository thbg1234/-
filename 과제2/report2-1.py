
number = int(input("숫자를 입력하십시오："))
for i in range(1, number+1):
    for j in range(i):
        print("*", end="")
    print()