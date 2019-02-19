import sys
import time
from tets import cal
import requests

#a = requests.get('https://www.python.org')
#print(a.content)

#print(sys.argv)
#print(time.localtime())

def num(a):
    print(cal().cal3(a))
    print(cal().cal2(a))
    print(cal().cal1(a))


num(9)