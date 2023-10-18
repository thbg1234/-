'''
2023.10.18
석홍신(202195056)
 설명 : 입력을 받아 맛있는 과일의 리스트를 만들자.
    
    좋아하는 과일 5개를 입력받아 리스트에 저장한다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단한다.
    
    추가 = append() 메소드
    찾기 = in 연산자

'''

fruits = []

for i in range(s):
    a=input(str(i+1)+"좋아하는 과일 입력:")
    fruits.append(a)
  
print("입력한 과일 리스트:")

favo_fruit = input("좋아하는 과일 하나를 입력:")

if favo_fruit in fruits :
    print(f'{favo_fruit}은(는) 당신이 좋아하는 과일입니다.')
else:
    print(f'{favo_fruit}은(는) 당신이 좋아하는 과일이 아닙니다.')