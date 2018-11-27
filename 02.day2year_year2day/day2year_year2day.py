# -*- coding: utf-8 -*-
#判断是否是闰年 (year能被4整除 and 不能被100整除) or year能被400整除

run = [31,28,31,30,31,30,31,31,30,31,30,31]
def runnian(year):
    if ((year % 4) ==0 and ((year % 100) != 0)) or (year % 400 == 0) :
        return 1
    else:
        return 0

def calculate1():
    i=0
    year, month, day = map(int, raw_input(u"请输入你要判断的年月日(中间用空格隔开)：\n").split())       # split  split()就是将一个字符串分裂成多个字符串组成的列表。split()当不带参数时以空格进行分割，当代参数时，以该参数进行分割
    global count
    count = day
    if runnian(year):
        run[1] = 29
    while i < (month-1):
        count += run[i]
        i = i + 1
    return year

def calculate2():
    i = 0
    global m
    global year2
    year2, day = map(int, raw_input(u"请输入你要判断的年份和天数 (中间用空格隔开)：\n").split())
    m = day
    if runnian(year2):
        run[1] = 29
    while m > run[i]:
        m = m - run[i]
        i = i+1
    return i+1

n = int( raw_input(u"输入数字选择实现功能：1.根据年月日判断天数 2.根据天数判断年月日\n") )
if n == 1 :
    year = calculate1()
    print u"这天是 %d 年的第 %d 天"%( year, count)
else :
    month = calculate2()
    print u"这天是 %d 年 %d 月 %d 日"%(year2 , month , m)
