"""
常用内置函数：
    ord()用来返回单个字符的序数或ASCII码；
    chr()用来返回介于0到255之间的某序数对应的字符；
    str()用来返回任意类型参数转换为字符串

"""

print(ord("a"), type(ord("a")))
print(ord("A"), type(ord("a")))

print(chr(97), type(chr(97)))
print(chr(65), type(chr(65)))

print(str(1234), type(str(1234)))
print(str([1, 2, 3, 4]), type(str([1, 2, 3, 4])))
print(str((1, 2, 3, 4)), type(str((1, 2, 3, 4))))


