# -*- coding: utf-8 -*-

#circulardoublelinklist


class Node(object):
	def __init__(self, data=None):
		self.elem = data
		self.next = None
		self.pre = None


class CircularLinkList(object):
	def __init__(self):
		node = Node(None)
		self.root = node
		node.next = node
		node.pre = node
		self.length = 0

	def __len__(self):
		return self.length

	def topnode(self):
		return self.root.next

	def tailnode(self):
		return self.root.pre

	def append_right(self, item):
		node = Node(item)
		tailnode = self.tailnode()

		tailnode.next = node
		node.pre = tailnode
		node.next = self.root
		self.root.pre = node

		self.length += 1

	def append_left(self, item):
		node = Node(item)

		node.pre = self.root
		node.next = self.root.next
		self.root.next.pre = node
		self.root.next = node

		self.length += 1

	def travel(self):
		cur = self.root.next

		while cur is not self.root:
			print(cur.elem)
			cur = cur.next

	def insert(self, index, item):
		node = Node(item)
		if index <= 0:
			self.append_left(item)
		elif index >= self.length:
			self.append_right(item)
		else:
			cur = self.root.next
			while index-1:
				index -= 1
				cur = cur.next
			node.next = cur.next
			node.pre = cur
			cur.next.pre = node
			cur.next = node
		self.length += 1

	def delete_item(self, item):
		cur = self.root.next
		while cur.elem is not item:
			cur = cur.next
		else:
			cur.next.pre = cur.pre
			cur.pre.next = cur.next
		self.length -= 1

if __name__ == '__main__':
	cll = CircularLinkList()
	node = Node(4)
	cll.append_left(1)
	cll.append_right(2)
	cll.append_right(3)
	cll.append_left(4)
	cll.insert(1, "a")
	cll.delete_item("a")
	cll.travel()
	print(cll.__len__())