"""
列表操作 4：
    连接 str.join(list)：用于将字符串序列中的元素以指定的字符连接生成一个新的字符串。
    大写 str.upper()：将字符串中的所有字母转为大写字母。
    小写 str.lower()：将字符串中的所有字母转为小写字母。
    替换 str.replace(old, new[, max])：将字符串中的old（旧字符串）替换成new(新字符串)，如果指定第三个参数max，则替换不超过max次。
    分割 str.split(sep = " ", maxsplit = str.count(sep))：通过sep (默认为空格)将str 分割成字符串列表，num 表示分割次数
    移除 str.strip([chars])：str 代表的是指定检索的字符串，chars 代表移除字符串头尾指定的字符，默认为空格。

"""

seq = ["r", "u", "n", "o", "o", "b"]
print("使用-连接：", "-".join(seq))
print("使用 连接：", "".join(seq))


field='do it now'
print("title: ", field.title())
print("upper: ",field.upper())
print("lower: ",field.lower())


field='do it now, do right now.'
print("原字符串：", field)
print("新字符串：", field.replace("do", "Just do"))


str = "this is string example....wow!!!"
print(str.split())
print(str.split("i", 1))
print(str.split("w"))


field='----do it now----'
print("原字符串：", field)
print("lstrip 新字符串：", field.lstrip("-"))
print("rstrip 新字符串：", field.rstrip("-"))
print("strip 新字符串：", field.strip("-"))

