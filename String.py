__author__ = 'Administrator'
'''
   转义
'''
s = 'Yes,he doesn\'t'
print(s + " have money!")

'''
    取长度
'''
print(len(s))

'''
    如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串：
'''
s2 = r'C:\some\name'
print(s2)

'''
    字符串可以使用 + 运算符串连接在一起，或者用 * 运算符重复：
'''
print('a'+'b', 'a'*3)


"""
    字符索引
"""
s3 = "This a S3"
print(s3[0], s3[2], s3[-1], s3[-2])

'''
    取子字符串
'''
print("取子字符串(0-4):", s3[0:4])
print("取子字符串(4以后):", s3[4:])
print("取子字符串(2以后):", s3[:2])