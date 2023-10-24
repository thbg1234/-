list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]
result = []
for num1 in list1:
    for num2 in list2:
        result.append(f"{num1}*{num2}={num1*num2}")
print(result)