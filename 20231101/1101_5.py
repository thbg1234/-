'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
    
'''

items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"골라":4,"색":5}

print(items.keys())

name = input ()

print('제고:',items[name])

print('제품 목록:',end =  '')
for key in items.keys():
    print(key,end='')
print()

name = input('제품의 이름 입력')
print('제고',items[name])

