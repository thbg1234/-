'''
2023.10.18
석홍신(202195056)
 설명 : 리스트 만들기
'''

fruits = ["딸기","사과","바나나"]
print("과일 목록",fruits)

fruits.append("수박")
print("과일 목록(수박 추가)",fruits)
fruits.append("망고")
print("과일 목록(망고 추가)",fruits)

fruits = fruits+["포도"]
print("과일 목록(포도 추가)",fruits)

num = [1,2,3]+[4,5,6]
print("숫자 리스트:",num)

num = [1,2,3]*3
print("숫자 리스트:",num)

print("과일 목록에 망고가 있나요?","망고" in fruits)

print("과일 리스트에 있는 과일 개수 : ", len(fruits))

print("과일 중 제일 좋아하는 과일은? ", fruits[0])

print("과일 중 제일 마지막 과일은? ", fruits[-1])

print("과일 중 가장 큰 과일은?(사전식 순서) ", max(fruits))

print("과일 중 가장 작은 과일은?(사전식 순서) ", min(fruits))

fruits.sort()   
print("오름차순 정렬 : ", fruits)

fruits.sort(reverse=True) 
print("내림차순 정렬 : ", fruits)

'''
    리스트를 원하는 모양으로 자르는 슬라이싱
'''
print("과일 목록 : ", fruits)
print("과일 리스트 중 2,3,4번 과일은? ", fruits[1:4])  
print("과일 리스트 중 1~3번 과일은? ", fruits[0:3])  
print("과일 리스트 중 1~3번 과일은? ", fruits[:3])  
print("과일 리스트 중 3번 과일부터 마지막까지 과일은? ", fruits[2:])  

print("과일 리스트 중 1,3,5번 과일은? ", fruits[::2]) 
print("과일을 거꾸로 출력" , fruits[::-1])


'''
    리스트의 원소 값을 자유롭게 조작해 보자.
'''
print()
print("과일 목록 : ", fruits)

fruits.insert(3, '두리안')
print("과일 목록(3번지에 두리안 추가) : ", fruits)

print("사과의 위치는? ", fruits.index('사과'))

fruits.append('사과')
print("과일 목록(마지막에 사과 추가) : ", fruits)

print("사과의 개수는? ", fruits.count('사과'))

'''
    리스트의 항목 삭제
'''
print()

fruits.remove('사과')  
print("과일 목록(사과 삭제 후) : ", fruits)

fruits.pop()   
print("과일 목록(마지막 과일 삭제) : ", fruits)

del fruits[0]   
print("과일 목록(포도(0번지) 삭제) : ", fruits)
