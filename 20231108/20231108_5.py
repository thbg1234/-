'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
'''


student_tuple = {'202195056','석홍신','010-1234-5678'},{'203242366','김나이','010-1427-3636'},{'203475763','장채아','010-2854-3887'}

student_dict = {}
for id_num,name ,phone in student_tuple:
    student_dict[id_num] = [name,phone]

for key,value in student_dict.items():
    print(key,":",value)

number = input("학번을 입력하십시오:")
print('이름',student_dict[number][0])
print('연락처',student_dict[number][1])

student_dict['202095001'].append(4,5)
student_dict['202095002'].append(3,8)
student_dict['202095003'].append(3,5)

for key ,value in student_dict.items():
    print(key,":",value)


print("전체 학생 평균 학점")
sum = 0
for key , value in student_dict.items():
    sun = sum + value[2]


print (f"평균:{(sum/3):.2f}")