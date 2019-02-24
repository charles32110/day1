# -*- coding: utf-8 -*-

'''
doublelinklist
'''

class Node(object):
	def __init__(self, data):
		self.elem = data
		self.pre = None
		self.next = None


class DoubleLinkList(object) :

	def __init__(self, node = None) :
		self.__head = node

	def __len__(self):
		length = 0
		cur = self.__head
		while cur:#1 true
			length +=1
			cur = cur.next
		return length

	def travel(self):
		cur = self.__head
		while cur:
			print (cur.elem, end = ' ')
			cur = cur.next

	def append(self, item):
		node = Node(item)
		if self.__head is None:
			self.__head = node
		else:
			cur = self.__head
			while cur.next:
				cur = cur.next
			else:
				cur.next = node
				node.pre = cur

	def insert(self, pos, item):
		node = Node(item)
		cur = self.__head
		if pos <= 0:
			node.next = self.__head
			self.__head = node
		elif pos >= len(self):
			self.append(item)
		else:
			while pos-1:
				pos -= 1
				cur = cur.next
			else:
				node.pre = cur
				node.next = cur.next
				cur.next.pre = node
				cur.next = node

	def delet_item(self, item):
		cur = self.__head
		if cur.elem is item:
			self.__head = cur.next
			if cur.next:
				cur.next.pre = None
		else :
			while cur.elem is not item :
				cur = cur.next
			else :
				cur.pre.next = cur.next
				if cur.next:
					cur.next.pre = cur.pre

	def delete_index(self, index):
		cur = self.__head
		if index <= 0:
			self.__head = cur.next
			cur.next.pre = None

		elif index >= len(self):
			while cur.next:
				cur = cur.next
			else:
				cur.pre.next = cur.next
		else:
			while index:
				index -=1
				cur = cur.next
			else:
				cur.pre.next = cur.next
				if cur.next:
					cur.next.pre = cur.pre

if __name__ == '__main__' :
	dll = DoubleLinkList()
	dll.append(1)
	dll.append(2)
	dll.append(3)
	dll.append(4)
	# dll.insert(0,'b')
	dll.delete_index(1)
	dll.travel()


	print('\n'+ str(dll.__len__()))















