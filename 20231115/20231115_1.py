'''
    작성일 : 2023년 11월 15일
    작성자 :석홍신(202195056)
    설명:문자열
'''

s='Happy Day!'
print(s[0])
print(s[6:10])
print(s[:-2])

s='Welcome to Python'
print(s.split())

s='2023.11.15'
print(s.split('.'))

s = 'Hello,World'
print(s.split('.'))
s = 'Welcome,to,Python, and,bla,bla         '
print(s.strip())
print([x.strip() for x in s.split('.')])

print(list('Hello,World!'))



print('.'.join(['apple','grape','banana']))
print('.'.join('010.1234.5678'))

print('010.1234.5678'.replace('.','-'))

s = 'hello world!'
print(s)


slist = list(s)
print(slist)

print(''.join(slist))

a_string ='Today as well,\n\t Have a Happy Day'
print(a_string)

word_list = a_string.split()
print(word_list)

refined_string =" ".join(word_list)
print(refined_string)


s = 'Hello World!'
print(s)
print(s.lower())
print(s.upper())


s = '    Hello,world!     '
print(s.strip())
print(s.lstrip())
print(s.rstrip)
s = '########Hello, World!#########'
print(s)
print(s.strip('#'))


s = 'www.silla.ac.kr'
print(s.find('.kr'))
print(s.find('x'))


print(s.count('.'))


