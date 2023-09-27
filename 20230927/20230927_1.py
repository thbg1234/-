'''설명 : 점수를 입력받아 학점을 출력하시오.
            90~100 : A학점
            80~89  : B학점
            70~79  : C학점
            60~69  : D학점
            0~59   : F학점
'''




num = int (input("第一次输入成绩："))
if num>89 and num<101:
    print("A")
elif num>79 and num<90:
    print("B")
elif num>69 and num<80:
    print("C")
elif num>59 and num<70:
    print("D")
else:
    print("F")

    print("：：：第二次成绩整理：：：")
    if(90<=num<=100):
        print("A")
    elif(num>=80 and num<=89):
        print("B")
    elif(num>=70 and num<=79):
        print("C")
    elif(num>=60 and num<=69):
        print("D")
    elif(num>=0 and num<=59):
        print("F")
    else :
        print("分数输入错误 ")


    print("：：：第三次成绩整理：：：")
    if 0<=num<=100:
        if num>89 and num<101:
           print("A")
        elif num>79 and num<90:
           print("B")
        elif num>69 and num<80:
           print("C")
        elif num>59 and num<70:
         print("D")
        else:
          print("F")

    else:
        print("输入错误")

    