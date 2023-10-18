'''
2023.10.18
석홍신(202195056)
 설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''


population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

print(f'서울 인구 : {population[1]}명')     
print(f'인천 인구 : {population[-1]}명')    

cities = population[0::2]             
print('도시 리스트 :', cities)

pops = population[1::2]               
print('도시 인구 리스트 :', pops)

pops = population[1::2]               
print(f'인구의 합 : {sum(pops)}명')
