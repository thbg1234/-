'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
    
'''

color_list =['red','green','blue','orange']

color =('red','green','blue','orange')

print(f"color: {color} ")

#color.append('black')

print ('color 튜플',color)
print ('color 튜플 중 2,3,4번은?',color[1:4])
print ('color 튜플 중 1,2,3번은?',color[:3])
print ('color 튜플 중 3-끝은?',color[2:])
print ('color 튜플 중 1,3,5번은?',color[::2])
print ('color 튜플 중 거꾸로 출력',color[::-1]) #反向输出

colors = color+color
print('colors튜플:',colors)
print('color튜플 을 10번 반복',color*10)