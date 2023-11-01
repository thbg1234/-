'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
    
'''

phone_book1 = {}

phone_book1 ['석홍신'] = '010-1234-5678'

print('phone_book1',phone_book1)

phone_book2={'student1':'010-9876-5432','석홍신':'010-1234-5678'}
print('phone_book2:',phone_book2)

phone_book3={}
phone_book3['석홍신']='010-1234-5678'
phone_book3['student1']='010-9876-5432'
phone_book3['student2']='010-3245-6462'
phone_book3['student3']='010-3266-6587'
phone_book3['student4']='010-2378-7345'

print('phone_book3:',phone_book3)


print()

print(phone_book3.keys())
print(phone_book3.values())
print(phone_book3.items())


print()
print("::phone_book3 item 출력::")
for name ,phone_num in phone_book3.items():
    print(name,':',phone_num)

print()
print("::phone_book3[keys]출력::")
for key in phone_book3.keys():
    print(key,":",phone_book3[key])

print()

print(print("key:value"))
person_dict = {'name':'석홍신','age':25,'class':'3학년'}

print('name:',person_dict['name'])
print('나이',person_dict['age'])

print()
print("::정렬::")
print(sorted(phone_book3))

print('::key를 기준으로 전세 정렬::')
sort_phone_book3 = sorted(phone_book3.items(),key = lambda x:x[0])
print(sort_phone_book3)

print('::key를 기준으로 전세 정렬::')
sort_phone_book3 = sorted(phone_book3.items(),key = lambda x:x[1])
print(sort_phone_book3)


print()

print('::함목 삭제::')
del phone_book3['석홍신']
print(phone_book3)

print('::전체 삭제::')
phone_book3.clear()
print(phone_book3)







