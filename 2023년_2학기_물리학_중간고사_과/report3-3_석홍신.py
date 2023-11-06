def Cel_202195056(celsius):  
    return round((celsius * 9/5) + 32, 2)  
  
def Fahl_202195056(fahrenheit):  
    return round((fahrenheit - 32) * 5/9, 2)  
  
temp = input("섭씨 또는 화씨온도를 입력하세요(27C 또는 27F) : ")  
if temp[-1] == 'C':  
    celsius = float(temp[:-1])  
    fahrenheit = Cel_202195056(celsius)  
    print(f"화씨온도 {celsius}C는 섭씨온도 {fahrenheit}F 입니다.")  
elif temp[-1] == 'F':  
    fahrenheit = float(temp[:-1])  
    celsius = Fahl_202195056(fahrenheit)  
    print(f"섭씨온도 {fahrenheit}F는 화씨온도 {celsius}C 입니다.")  
else:  
    print("온도를 잘 못 입력하셨습니다.")