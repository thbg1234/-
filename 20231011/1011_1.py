'''
2023.9.27
석홍신(202195056)
 설명 : def
'''


def address():
    print ("부산시 사상구")
    print ("괘법동 산 1-1번지")
    print ("신라대학교 국제교육관 552호")
address()
address()
address()



print("인지와 메개변수")
def welcome(name):
    print(name,"님 안녀하세요")
    print(f"(name)님 안녀하세요")
    print("{}님 안녀하세요".format(name))
welcome("석홍신")