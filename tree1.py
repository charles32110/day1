# -*- coding: utf-8 -*-


class Node(object):
	def __init__(self, item):
		self.elem = item
		self.l_child = None
		self.r_child = None


class Tree(object):
	def __init__(self):
		self.root = None

	def __add__(self, item):
		node = Node(item)
		if self.root is None:
			self.root = node
			return
		else:
			queue = list()
			queue.append(self.root)
			while queue is not None:
				cur_node = queue.pop(0)
				if cur_node.l_child is None:
					cur_node.l_child = node
					return
				else:
					queue.append(cur_node.l_child)
				if cur_node.r_child is None:
					cur_node.r_child = node
					return
				else:
					queue.append(cur_node.r_child)

	def breath_travel(self):
		if self.root is None:
			return
		queue = []
		queue.append(self.root)
		while queue :
			cur_node = queue.pop(0)
			print (cur_node.elem,end = '  ')
			if cur_node.l_child is not None:
				queue.append(cur_node.l_child)
			if cur_node.r_child is not None:
				queue.append(cur_node.r_child)

	def pre_order(self,root_node):
		if root_node is None:
			return
		print(root_node.elem,end = '  ')
		self.pre_order(root_node.l_child)
		self.pre_order(root_node.r_child)

	def in_order(self,root_node):
		if root_node is None:
			return
		self.in_order(root_node.l_child)
		print(root_node.elem,end = '  ')
		self.in_order(root_node.r_child)

	def pos_order(self,root_node):
		if root_node is None:
			return
		self.pos_order(root_node.l_child)
		self.pos_order(root_node.r_child)
		print(root_node.elem,end = '  ')

# use the stack
	def preoder(self,root):
		if root is None:
			return
		stack = []
		while root :



if __name__ == '__main__' :
	tree = Tree()
	tree.__add__(1)
	tree.__add__(2)
	tree.__add__(3)
	tree.__add__(4)
	tree.__add__(5)
	print('breath')
	tree.breath_travel()
	print('\npreorder')
	tree.pre_order(tree.root)
	print('\ninorder')
	tree.in_order(tree.root)
	print('\nposorder')
	tree.pos_order(tree.root)


