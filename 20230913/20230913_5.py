'''
    작성일 : 2023년 9월 13일
    작성자 : 석홍신(202195056)
    설명 : 90페이지 문제 3.9 
          평균 시속과 이동시간을 입력받아 
          이동 시간은 시,분,초 단위로 출력하고, 
          이동한 거리를 계산하여 출력하시오.

오늘의 마지막 문제.
해결한 사람은 과제 게6시판에 제출, 깃허브에 업로드 후 퇴근!
'''



average_speed = float(input("평균 시속（km/h）을 입력하세요:"))
travel_time = float(input("이동 시간（h）을 입력하세요:"))
distance = average_speed * travel_time
print("평균 시속：", average_speed, "km/h")
print("이동 시간：", travel_time, "h")
print("이동 거리：", distance, "km")
