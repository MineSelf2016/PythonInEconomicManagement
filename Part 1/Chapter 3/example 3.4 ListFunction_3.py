"""
列表操作 3：
    排序 list.sort(cmp=None, key=None, reverse=False)
    反转 list.reverse()

"""
Guests = ["David", "Tom", "Alex", "Jim", "Bob", "Alice"]
Guests.sort()
print(Guests)

# 指定参数key，按字符串由短到长排序
Guests.sort(key = len)
print(Guests)


# 指定参数key，按最后一个字符大小排序
Guests.sort(key = lambda value : value[-1])
print(Guests)

Guests.reverse()
print(Guests)

