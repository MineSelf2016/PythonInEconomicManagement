"""
根据华氏和摄氏温度定义，转换公式如下：
          C = ( F – 32 ) / 1.8
          F = C * 1.8 + 32
        其中，C表示摄氏温度，F表示华氏温度

"""

val = input("请输入带温度表示符号的温度值（例如32C 或 32F）: ")

if val[-1] in ["C", "c"]:
    F = float(val[0 : -1]) * 1.8 + 32
    print("F = ", F, "F")
elif val[-1] in ["F", "f"]:
    C = (float(val[0:-1]) - 32) / 1.8
    print("C = ", C, "C")
else:
    print("请输入正确格式")
