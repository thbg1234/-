'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)

'''



partyA = set(["Park","Kim","lee"])
partyB = set(["Park","Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같다:",partyA.intersection(partyB))
print("A,B에 참석한 사람",partyA|partyB)
print("A,B에 중복없이 참석한 사람",partyA^partyB)
print("A만 참석한 사람",partyA-partyB)