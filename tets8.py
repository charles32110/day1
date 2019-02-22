# -*- coding: utf-8 -*-
"""
单链表总结

"""


class Node(object) :
	'''init the the  element'''

	def __init__(self,data) :
		self.elem = data
		self.next = None


class SingleLinkList(object) :
	'''get the function '''
	def __init__(self) :
		self._head = None

	def __len__(self):
		length = 0
		cur = self._head
		while cur:
			length +=1
			cur = cur.next
		return length

	def append(self,item):
		node = Node(item)
		if self._head is None:
			self._head =node
		else:
			cur = self._head
			while cur.next:
				cur = cur.next
			else:
				cur.next = node

	def get(self,index):
	# search the element from the index

		if index >=0 & index < len(self):
			cur = self._head
			while index:
				index -=1; cur = cur.next
			else:
				return cur.elem
		else:
			return False

	def search(self,item):
		# search the element from the content
		cur = self._head
		while cur :#is not None
			if cur.elem ==item:
				return True
			else:
				cur = cur.next
		else:
			return  False

	def delete_elem(self,item):
		cur = self._head
		pre = None
		if  cur.elem == item:
			self._head = cur.next
		else:
			while cur is not None:
				if cur.elem == item:
					pre.next = cur.next
					break
				else:
					pre = cur
					cur = cur.next

	def delete_index(self,index):
		pre = None
		cur = self._head
		if index <=0:
			self._head= cur.next

		elif len(self) <= index:
			while cur:
				if cur.next ==None:
					pre.next = cur.next
					break
				else:
					pre = cur
					cur = cur.next




		else:
			while index-1:
				index -=1;pre = cur;cur = cur.next
			else:
				pre.next = cur.next

	def insert(self,pos,item):
		node = Node(item)
		if pos <= 0:
			node.next = self._head
			self._head = node

		elif pos > len(self):
			self.append(item)

		else:
			cur = self._head
			while pos-1:
				pos -=1
				cur = cur.next
			node.next = cur.next
			cur.next = node

	def travel(self):
		cur = self._head
		while cur:
			print (cur.elem, end = ' ')
			cur = cur.next

	def main(self):
		self.append(1)
		ll.append(2)
		ll.append(3)
		ll.append('a')
		ll.append('b')
		print(ll.search("c"))
		print(ll.get(2))
		ll.travel()
		# ll.delete_elem('b')
		print('\n')
		ll.insert(2, 'tets')
		ll.delete_index(10)
		ll.travel()


if __name__ == '__main__':
	ll = SingleLinkList()
	ll.main()


















