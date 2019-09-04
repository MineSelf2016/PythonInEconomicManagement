"""
列表操作 1：
    索引：[index]方法，返回指定下标index的元素值。
    切片：[start:stop:step]，返回指定范围的元素构成的新列表。

"""

Guests = ["David", "Tom", "Alex", "Jim", "Bob"]
print("Guests: ", Guests)
print("Guests[0]: ", Guests[0], "\nGuests[1]: ", Guests[1], "\nGuests[-1]: ", Guests[-1])

message = Guests[0].upper() + ", welcome to our Python class!"
print("message: ", message)

number = [i for i in range(1, 11)]
print("number: ", number)
print("number[1:2] : ", number[1 : 3])
print("number[-3:-1]: ", number[-3 : -1])
print("number[-3: ]: ", number[-3: ])

# 显式设置步长
print("number[0::2]: ", number[0::2])
print("number[1::2]: ", number[1::2])
print("number[-2::-2]", number[-2::-2])
print("number[-1::-2]", number[-1::-2])


# for each 循环
for guest in Guests: 
    print(guest, guest.upper())
    print("Welcome to our Python class!")




