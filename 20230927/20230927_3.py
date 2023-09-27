'''
2023.9.27
석홍신(202195056)
설명 : 반복문 for 사용하기
'''
print("输出5次我的名字")
for i in range(5):
    print(i,"석홍신")

print("输出5次我的名字")
for i in (1,2,3,4,5):
    print(i,"석홍신")

print("리스트로 구구단의 19단 출력")
for num in (1,2,3,4,5,6,7,8,9):
    print(num,"19x(num)=(19num)")

print("输出文章内容")
for i in "Hello" :
    print("i=",i)

print("BTS ,엠버,명단,출력")
bts = {'뷔','제이흠','알엠','정국','진','지민','슈가'}
for i in bts:
    print(i)