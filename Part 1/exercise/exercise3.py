"""
题目：输入某年某月某日,判断这一天是这一年的第几天（需考虑闰年情况）。
输入：2016 1 1 输出 1
输入：2016 3 2 输出 62
"""

#%%
year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

days = 0

months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
days = sum(months[:month]) + day

#%%
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100) != 0)) and month >= 3:
    print("leap")
    days += 1

#%%
days

#%%
