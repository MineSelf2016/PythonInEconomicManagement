time = "2年半"
hobby_1 = "唱"
hobby_2 = "跳"
hobby_3 = "rua"
hobby_4 = "篮球"

print("大家好，我是练习时长{}的个人练习生CXK, 喜欢{}、{}、{}、{}，music~~".format(time, hobby_1, hobby_2, hobby_3, hobby_4))
print("大家好，我是练习时长{0}的个人练习生CXK, 喜欢{1}、{2}、{3}、{4}，music~~".format(time, hobby_1, hobby_2, hobby_3, hobby_4))
print("大家好，我是练习时长{time}的个人练习生CXK, 喜欢{hobby_1}、{hobby_2}、{hobby_3}、{hobby_4}，music~~".format(time = time, hobby_1 = hobby_1, hobby_2 = hobby_2, hobby_3 = hobby_3, hobby_4 = hobby_4))
print("为什么{name}的鸡那么美".format(name = "'CXK'"))
print('为什么\'' + 'CXK' + '\'的鸡那么美')

# 对于浮点数"0.333"，保留小数点(.)后3 位
print("{0:.3f}".format(1/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用(^)定义 "___hello___"字符串长度为 11
print("{0:_^11}".format("hello"))
# 基于关键词输出"Swaroop wrote A Byte of Python"
print("{name} wrote {book}".format(name = "swaroop".title(), book = "A Byte of Python"))


