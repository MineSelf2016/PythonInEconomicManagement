"""
列表操作 2：
    成员资格 in；
    添加元素 list.append(obj)，在列表尾部添加元素，insert(index, obj)，在列表指定位置添加元素；
    删除元素 list.pop(index = 0)，移除列表中的最后一个元素并且返回该元素，remove(obj)，移除列表中某个值的第一个匹配项；
    长度 len(list)
    最大值 max(list)；
    最小值 min(list)；
    求和 sum(list)。

"""
greeting = "Hello, world"
print("w" in greeting)
print("a" in greeting)


Guests = ["David", "Tom", "Alex", "Jim", "Bob"]

print("Guests: ", Guests)
Guests.append("Alice")

Guests.insert(0, "Swift")
print(Guests)

Guests.remove("Jim")
print(Guests)

# 通过下标修改元素
Guests[-1] = "King"
print(Guests)


arr = [33, 55, 77, 11, 44, 11, 11]
print("arr's length: ", len(arr))
print("arr's max item: ", max(arr))
print("arr's min item: ", min(arr))
print("arr's sum: ", sum(arr))
