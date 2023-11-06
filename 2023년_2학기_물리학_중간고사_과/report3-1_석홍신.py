
list1_202195056 = [1,2,3,4,5]
list2_202195065 = []
n=0
while n<len(list1_202195056):
    print(list1_202195056[n],end='')
    a = str(input('번 과일을 입력하세요:'))
    list2_202195065.append(a)
    n+=1
m=0
while m<len(list1_202195056):
    print(list1_202195056[m],'.',list2_202195065[m])
    m+=1