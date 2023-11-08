'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
    설명:set()
'''

number = set()
number1 = {2,1,3}
print("집합",number1)

number2= set([1,2,3,1,2])
print("집합",number2)

text1 = set("asdfasdf")
print('text1:',text1)

numbers = {2,4,5,1,2}
if 1 in numbers:
    print('numbers',numbers)

numbers = {9,1,5,2,4,7,6,3,4,9,1}
for num in numbers:
    print(num,end='')

print()


for num in sorted(text1):
    print(num,end='')

print()

numbers.add(100)
print(numbers)
for num in sorted(numbers):
    print(num,end='')

print()


numbers.remove(100)
print(numbers)


