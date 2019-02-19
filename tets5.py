

class MyTest(object):

    __value= 0

    def __init__(self):
        self.name = "dueape"
        self.kind = "it"
        self.age = 10
        self.__value = 10000


    def test1(self):
        return ('hello world', self.name)

    def intr(self):
        return ("my name is" + self.name + "and I am " + str(self.age) + "years old")

    def test2(self):
        return (self.__value)



class MyClass(MyTest):
    def __init__(self,language):
        MyTest.__init__(self)
        self.name = language


    def tets2(self):
        print(self.name  + "  can help you")


    def test1(self):
        print(self.name +  "say hello to you")




x = MyClass("DUEAPE PYTHON")

x.test1()
#print(x.test2())
