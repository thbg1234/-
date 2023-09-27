'''2023.9.27
석홍신(202195056)
설명 :  터틀 그래픽으로 여러 개의 원을 그려보자 
'''

import turtle as t

#t.circle(100)
for count in range(10):
    t.circle(100)
    t.left(360/10)
t.mainloop()
t.done()