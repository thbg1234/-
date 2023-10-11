import random
def getMinMax():
    i=0
    a1=0
    a2=100
    while(i<10):
        num=random.randint(10,99)
        i+=1
        print(num)
        if(a1<num):
            a1=num
        if(a2>num):
            a2=num
    return a1,a2
max_value, min_value = getMinMax()
num1 = input("Max인지 Min인지 알고 싶어요: ")
if num1 == 'Max':
    print(max_value)
elif num1 == 'Min':
    print(min_value)
else:
    print("잘못된 입력입니다.")

