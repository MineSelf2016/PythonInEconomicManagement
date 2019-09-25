"""
题目：打印出所有的水仙花数，所谓“水仙花数”是指一个三位数，其各位数字的立方和等于该数本身。
例如：153 是一个“水仙花”数，因为 153 == 1 ** 3 + 5 ** 3 + 3 ** 3

"""

#%%
for x in range(100, 1000):
    tmp = x
    i = tmp % 10
    j = (tmp // 10) % 10
    k = (tmp // 100 % 10)
    if x == i ** 3 + j ** 3 + k ** 3:
        print(x)

#%%
