'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
'''



student_tuple=[('211101','강이안','010-123-1111'),('211102','박동민','010-123-2222'),('211103','김수정','010-123-3333')]

for student in student_tuple:
    print(f"{student[0]}:{student[1]}")

input_ids = input("학번을 입력하십시오：")
input_ids = input_ids.split(',')

for id in input_ids:
    for student in student_tuple:
        if id == student[0]:
            print(id,"학생은 "f"{student[1]}이며 전화번호는 {student[2]}입니다.")
