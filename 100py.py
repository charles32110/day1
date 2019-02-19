#coding:utf-8


#1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#a b c
'''
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and b != c and a != c:
                print(a,b,c)


list = [1,2,3,4]



def permutations(arr, position, end):
    if position == end:
        print(arr)

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]

for i in list:
    list2 = list[i+1:]+list[:i]
    permutations(list2, 0, len(list2))

'''
'''
2.企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
0_________-10______20 ____40___60___100____


a = int(input("输入额度： "))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if a > arr[idx]:
        r += (a-arr[idx])*rat[idx]
        #print ((a-arr[idx])*rat[idx])
        a = arr[idx]
print(r)
'''



'''
3.输入某年某月某日，判断这一天是这一年的第几天？

jan 4  第四天
feb 4   31+4
31 +28 + 31

x = int (input("输入年份："))
y = int(input("输入月份："))
z = int(input("输入日子："))

month= [1,2,3,4,5,6,7,8,9,10,11,12]
if x%4 == 0:
    a = 29
else:
    a = 28
month_day = [31,a,31,30,31,30,31,31,30,31,30,31]
if y in month and z <= month_day[y-1]:
    y = y-1
    while y > 0:
        y =y -1
        z += month_day[y]
    print("this is %dth day"%z)
else:
    print("wrong day")
'''
'''
4.输入三个整数x,y,z，请把这三个数由小到大输出。


list4 =[]
for i in range(3):
    list4.append(input("输入%s数"%(i+1)))
list4.sort()
print(list4)
'''

'''
5.递归斐波那契数列
1,1,2,3,5////
a = 1 b =1
a = b , b = a+b

def fib(n):
    a= 1
    b = 1
    list = []
    for i in range(n-1):
        a,b = b ,a+b
        list.append(a)
    return list
print(fib(8))



def fib1(n):
    a = 1
    b = 1
    if n ==1 or n ==2:
        return 1
    return fib1(n-1)+fib1(n-2)

print(fib1(4))
'''
'''
6.输出 9*9 乘法口诀表。
for a in range(10):
    for b in range(1,a+1):
        print("%s*%d = %d\n"%(a,b,a*b))
'''

'''
time模块
7.暂停一秒输出，并格式化当前时间。
import time
print(time.strftime("%Y-%M-%d  %H:%M:%S",time.localtime(time.time())))
time.sleep(3)
print(time.strftime("%Y-%M-%d  %H:%M:%S",time.localtime(time.time())))
'''
'''
8打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
求其100-999中的所有水仙花数

abc = a**3+b**3+c3

1+ 125 +27

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if a**3+b**3+c**3 == 100*a+10*b+c:
                print(a,b,c)

'''

'''
9.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

scr = int(input("输入成绩："))
if scr >=90:
    print("a")
elif scr <60:
    print('c')
else:
    print('b')
'''
'''
10.利用递归方法求5!。

def ter(n):
    sum = 0
    if n ==0:
        sum =1
    else:
        sum = n * ter(n-1)
    return  sum

print(ter(2))
'''
'''
11.递归的方法求1+2!+3!+...+20!


def perm1(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n*perm1(n-1)
    return sum
x = 0
for i in range(1,21):
    x += perm1(i)
print(x)

def perm1(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n*perm1(n-1)
    return sum


def perm2(n):
    if n ==0:
        sum = 0
    else:
        sum = perm1(n) +  perm2(n-1)
    return sum

print(perm2(20))
'''

'''
12.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def rever(s,l):
    if l == 0:
        return
    print(s[l-1])
    rever(s,l-1)
s = input("输入字符串：")
l = len(s)

rever(s,l)
'''

'''
13.有5个人坐在一起，问第五个人多少岁？
他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。
请问第五个人多大？
利用递归

a > b >c >d >e


def name(n):
    if n ==1:
        c  = 10
    else:
        c = name(n-1)+2
    return c

print(name(4))
'''












'''
14.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
利用递归全排序
a,b,c

def permutations(arr, position, end):
    if position == end:
        print(arr)

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]13
arr = [1,2,3,4]
permutations(arr,0,len(arr))
'''


'''
15.统计 1 到 100 之和。


def perm(n):
    sum =0
    if n ==1:
        sum =1
    else:
        sum = n + perm(n-1)
    return sum

print(perm(2))
'''


'''
16.尾数前移，求一个数个位为6.将6提到这个数的首位所得新数是这个数的4倍

n6   x 4 = 6n   600 +n  10** len(n)
153846
for n in range(1,100000):
    if 10**len(str(n))*6 +n == 4*(10*n+6):
        print(10*n+6)
'''


'''
17.自守数,一个数的平方，末尾还是这个数。
5**2 = 25    6**2 = 36

for i in range(1,1000):
    if (i**2)%(10**len(str(i-1))) == i :
        print(i)
'''

'''
18.等差数列

1 +3+5

def nums(start, x, n):
    if n ==1:
        return  start
    else:
        num = x + nums(start,x,n-1)
    return (num)
for i in range(1,10):
    print(nums(1,3,i))
'''

'''

19.杨辉三角
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]


def term(rows):
    for i in range(rows):
        value = 1
        list =[value]
        for j in range(i):
            value = value*(i-j)*1/(j+1)
            list.append(int(value))
        print(list)
term(7)

'''


'''
20判断是否为回文数（列表操作）
12321

x = input("输入你想测验的数：")
if x == x[::-1]:
    print('right')
else:
    print("wrong")
'''


















