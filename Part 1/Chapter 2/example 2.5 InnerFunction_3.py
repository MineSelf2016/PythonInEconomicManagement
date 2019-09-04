"""
常用内置函数：
    str()：使用函数str()将数字类型变成字符类型，然后进行字符串的拼接。

"""

year = 2019

# 报错，字符串类型不能与int 类型做加法
# message = "Goodbye, " + year
# 使用str() 将int 类型转换为字符串类型
message = "Goodbye, " + str(year - 1) + "!"

print(message)

