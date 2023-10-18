'''
2023.10.18
석홍신(202195056)
 설명 : 리스트의 객체 생성과 참조
'''


fruits1= ["딸기","수박","바나나"]

fruits2 = fruits1

print("fruits1:",fruits1)
print("fruits2:",fruits2)

fruits2[1] = "망고"

print("fruits1:",fruits1)
print("fruits2:",fruits2)

print("fruits1의 id:",id(fruits1))
print("fruits2의 id:",id(fruits2))

fruits2 = list(fruits1)
print("::내용 복제 후 2::")
print("fruits1:",fruits1)
print("fruits2:",fruits2)

print("fruits1의 id:",id(fruits1))
print("fruits2의 id:",id(fruits2))

fruits3 = fruits1[:]

print(":: 내용 복제 후 2 ::")
print("fruits1 : ", fruits1)   
print("fruits3 : ", fruits3)

print("fruits1의 id : ", id(fruits1))  
print("fruits3의 id : ", id(fruits3))

fruits3[0] = '수박'  
print(":: fruits3의 0번지에 수박으로 내용 바꾼 후 ::")
print("fruits1 : ", fruits1)   
print("fruits3 : ", fruits3)
