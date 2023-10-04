'''
2023.9.27
석홍신(202195056)
 설명 : 
'''

word= input('단어를 입력하시오')
print("::break1::")
for i in word:
    if i=='a' or i =='e' or i=='i' or i=='a' or i== 'u':
        break
    else:
        print(i,end='')

print ("::break2::")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        continue
    print (i,end='')