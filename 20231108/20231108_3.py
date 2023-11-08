'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
'''


numa = {1,2,3}
numb = {3,4,5}

print(numa|numb)
print(numa.union(numb))
print(numa&numb)
print(numa.intersection(numb))
print(numa-numb)
print(numa.difference(numb))
print(numa^numb)
print(numa.symmetric_difference(numb))