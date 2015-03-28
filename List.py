__author__ = 'Administrator'
'''
    List列表
'''
MyList1 = ['b', 1, 2]

# 打印list
print(MyList1)

# 打印其中一个
print(MyList1[0])

MyList1[0] = 0

# 改变List其中一个值
print("MyList[0] Is:  ", MyList1[0])

# 集合相加
MyList2 = MyList1 + [3, 4]
print(MyList2)

# 集合加到指定位置
MyList2[2:4] = [2, 3, 4]
print(MyList2)

# 删除集合指定的位置
MyList2[4:5] = []
print(MyList2)

MyList2.append(5)
print(MyList2)
