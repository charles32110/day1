# -*- coding: utf-8 -*-
from tets11 import CircularLinkList


class Deque(CircularLinkList) :
	def __init__(self) :
		super().__init__()

	def append_r(self,item):
		return self.append_right(item)

	def append_l(self,item):
		return self.append_left(item)

	def pop_l(self):
		item  = self.topnode()
		self.delete_item(item.elem)
		return item.elem

	def pop_r(self):
		item  = self.tailnode()
		self.delete_item(item.elem)
		return item.elem

	def len(self):
		return self.length


if __name__ == '__main__' :
	dq = Deque()

	dq.append_l(1)
	dq.append_l(2)
	dq.append_l(3)
	print(dq.pop_l())
	print(dq.pop_r())
