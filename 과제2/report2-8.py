fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'meion']
max_length = max(len(fruit) for fruit in fruit_list) 
fruit_list2 = [fruit for fruit in fruit_list if len(fruit) != max_length] 
print(fruit_list2)

fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'meion']
length_list3 = [len(fruit) for fruit in fruit_list]  
print("banana:문자열의 길이:",length_list3[0])
print("orange:문자열의 길이:",length_list3[1])
print("kiwi:문자열의 길이:",length_list3[2])
print("apple:문자열의 길이:",length_list3[3])
print("melon:문자열의 길이:",length_list3[4])