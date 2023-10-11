'''
2023.9.27
석홍신(202195056)
 설명 : 함수에 일을 시키고 그 값을 받아 오기
'''


print("::리턴값이 있는 함수::")

def area(radius):
    result=3.14*radius**2
    return result


result = area(3)
print (f"")

print()
print()

r=int(input("input"))
result = area(r)
print(f"")

print(f"")