'''
    작성일 : 2023년 11월 15일
    작성자 :석홍신(202195056)
'''


text = "There's a reason some people are working to make it harder to vote,\
especially for people of color. \
    It’s because when we show up, things change."

print(len(text))


text2 = text.split()
print(text2)
print('word1 count:',len(text2))

#使用python完成下列要求
#用空格分隔第28个小写单词输出
#判断第29个单词是kt还是Samsung还是LG还是SKT输出
#如果是KT,Samsung,LG,SKT，则替换为**输出
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'





text1 = text.split()
if len(text1) >= 28:
    print("28th word:", text1[27].lower())

    if len(text1) >= 29:
        text1_29 = text1[28]
        if text1_29.lower() in ['kt', 'samsung', 'lg', 'skt']:
            print("29th word:", "**")
        else:
            print("29th word:",text1_29)

text2 = text.replace('SKT','**')
text2 = text.replace('KT','**')
text2 = text.replace('Samsung','**')
text2 = text.replace('LG','**')

print(text2)

print('----------------------------------------------------'）

text_lower = text




