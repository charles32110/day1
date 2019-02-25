# -*- coding: utf-8 -*-

'''form a que with the singlelinkedlist'''
from tets8 import SingleLinkList


class Que_1(object) :
	'''text'''

	def __init__(self) :
		self.item_linkedlist = SingleLinkList()

	def __len__(self):
		return len(self.item_linkedlist)

	def push(self,item):
		return self.item_linkedlist.append(item)

	def pop(self):
		if len(self) <= 0:
			return ("empty queue")
		else:
			a = self.item_linkedlist.get(len(self)-1)
			self.item_linkedlist.delete_elem(a)
			return a


class Que_2(SingleLinkList) :
	'''text'''

	def __init__(self) :
		super().__init__()

	def len(self):
		return self.__len__()

	def push(self,item):
		return self.append(item)

	def pop(self):
		cur = self._head
		self._head = cur.next
		return cur.elem

if __name__ == '__main__' :
	q = Que_2()
	q.push(1)
	q.push(2)
	q.push(3)
	print(q.__len__())
	print(q.pop())
	print(q.pop())
