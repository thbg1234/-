'''작성일 : 2023년 9월 13일
   작성자 : 석홍신(202195056)
    설명 : 직각 삼각형의 빗변의 길이를 구하시오.
'''
bottom = int(input('직각삼각형의 밑변의 길이를 입력하시오: '))
height = int(input('직각삼각형의 높이를 입력하시오: '))
hypotenuse = (bottom ** 2 + height ** 2) ** 0.5
print('빗변은', hypotenuse, '입니다')
