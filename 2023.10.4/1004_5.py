'''
2023.9.27
석홍신(202195056)
 설명 : 
'''
num = 0
sum = 0
a='yes'
while a=='yes':
    num=int(input("숫자를 입력하시오:"))
    sum +=num
    a=input('계속?(yes/no)')

print('합계는:',sum)
