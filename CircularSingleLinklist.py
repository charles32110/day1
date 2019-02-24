# -*- coding: utf-8 -*-

#circularsinglelinklist

class Node(object):

	def __init__(self,data):
		self.elem = data
		self.next = None


class CircularLinkList(object) :

	def __init__(self,node = None) :
		self.__head = None
		if node:
			node.next = node

	def __len__(self):
		length = 1
		cur = self.__head
		while cur.next is not self.__head:
			length +=1
			cur = cur.next
		return length

	def append(self,item):
		node = Node(item)
		cur = self.__head
		if self.__head is None:
			self.__head = node
			node.next = self.__head
		else:
			while cur.next is not self.__head:
				cur = cur.next
			else:
				cur.next = node
				node.next = self.__head

	def travel(self):
		cur = self.__head
		while cur.next is not self.__head:
			print(cur.elem,end =  ' ')
			cur = cur.next
		print(cur.elem)

	def search(self,item):
		cur = self.__head
		while cur.next is not self.__head:
			if  cur.elem is item:
				return True
			else:
				cur = cur.next
		else:
			if  cur.elem is item:
				return True
			else:
				return False
	def delete_item(self,item):
		if self is None:
			print ("empty list")
		cur = self.__head
		pre = None
		while cur.next is not self.__head:
			if cur.elem is item:
				if cur is  self.__head:
					rear = self.__head
					while rear.next is not self.__head:
						rear = rear.next
					else:
						self.__head = cur.next
						rear.next = self.__head
						break
				else:
					pre.next = cur.next
					break
			else:
				pre = cur
				cur = cur.next
		else:
			if cur.elem is item:
				if cur ==self.__head:
					self.__head =  None
				else:
					pre.next = cur.next


if __name__ == '__main__' :
		cll = CircularLinkList()
		cll.append(1)
		cll.append(2)
		cll.append(3)
		print(cll.__len__())
		cll.travel()
		cll.delete_item(3)
		print('\n')
		cll.travel()
