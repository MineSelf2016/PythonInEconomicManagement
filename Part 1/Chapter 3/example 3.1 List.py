"""
通用列表：
    列表元素可以是任何类型，且元素间可以没有任何关系

字符串列表：
    全部列表元素均为字符串的我们简称为字符串列表，如 ['This', 'is', 'a', 'bike.']

数字列表：
    全部列表元素均为数字的我们简称为数字列表，如 [62, 65, 65, 64, 64, 63, 62, 63, 63, 63, 63, 62]

"""

print(['A','B','C','D','E','F','G'])

print([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

print(['A', 'B', 'C', 7, 8, 9])

print([[1, 2, 3], 'hello', 88, True, False])



_str = "This is a bike."
str_list = _str.split(" ")

print("字符串为 ", _str)
print("字符串列表为 = ", str_list)


weight = [62, 65, 65, 64, 64, 63, 62, 63, 63, 63, 63, 62]
sales = [1000, 2100, 1500, 3400, 5600, 4000, 5000]

print("weigh = ", weight)
print("sales = ", sales)

