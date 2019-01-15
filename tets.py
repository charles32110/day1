#make the module of the package and class mode


import math
class cal(object):

    def cal1(self,x):
        x = x*x
        return x
    def cal2(self,x):
        x = x+x
        return x
    def cal3(self,x):
        x = math.sqrt(x)
        return x
if __name__=='__main__':
    cal()

