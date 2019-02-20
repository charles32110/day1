# -*- coding: utf-8 -*-

"""
data structure and algrim

"""


'''
*/ **
python -m pdb xx.py


class tets(object):


    def tets1(self,normal):
        print("this is just %s" %normal)

    def tets2(self,normal, *args):
        print("this is just %s" %normal)

        if not args == -1 :
            for arg in args:
                print("it is additional func arguement %s:"%arg)
    def tets3(self,normal1,**kwargs):
        print("this is just %s" %normal1)
        for key, value in kwargs.items():
            print("{} = {}".format(key,value))

    def tets4(self,normal , *args,**kwargs):
        print("this is just %s" % normal)
        for arg in args:
            print("it is additional func arguement %s:" % arg)
        for key, value in kwargs.items():
            print("{} = {}".format(key, value))

#def tet5(selfn,normal, **kwargs,*args):
if __name__ == '__main__':
    t = tets()
   # t.tets2("normal func","python",'java','scala','anaconda')
    t.tets4('java','scala','spider',name = 'python',value = 'first language')

'''

'''SingleLinkList'''
class Node (object):

	def __init__ ( self,elem):
		self.elem = elem
		self.next = None

class SingleLinkList (object):
	def __init__(self,node = None):
		self._head = node

	def  check( self ):
		return self._head == None

	def __len__(self):
		pre = self._head
		length = 0
		while pre:
			length +=1
			pre = pre.next
		return length

	def travel(self):
		cur = self._head
		while cur:
			print(cur.elem,end = ' a')
			cur = cur.next

	def append( self ,item):
		node = Node(item)

		if  self.check():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert( self, ):
		pass

	def reverse( self ):
		pass

	def delete(self):
		pass




if __name__ == '__main__':
	s = SingleLinkList()

	s.check()
	s.append(1)
	s.append(2)
	s.append(3)

	s.travel()
