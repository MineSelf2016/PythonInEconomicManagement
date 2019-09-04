"""
不同操作数类型时，乘法运算的结果。

"""

print(2 * 3)
print(2.0 * 3)
print((3 + 4j) * 2)
print((3 + 4j) * (3 - 4j))
print("1" * 5)
print("a " * 10)
print([1, 2, 3] * 3)
print(list(map(lambda x : x * 3, [1, 2, 3])))
print(tuple(map(lambda x : x * 3, (1, 2, 3))))
print(3 * "a")