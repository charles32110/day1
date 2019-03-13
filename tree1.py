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
		while queue:
			cur_node = queue.pop(0)
			print ( cur_node.elem, end = '  ' )
			if cur_node.l_child is not None:
				queue.append(cur_node.l_child)
			if cur_node.r_child is not None:
				queue.append(cur_node.r_child)

	def pre_order(self, root_node):
		if root_node is None:
			return
		print(root_node.elem, end = '  ')
		self.pre_order(root_node.l_child)
		self.pre_order(root_node.r_child)

	def in_order(self, root_node):
		if root_node is None:
			return
		self.in_order(root_node.l_child)
		print(root_node.elem, end = '  ')
		self.in_order(root_node.r_child)

	def pos_order(self, root_node):
		if root_node is None:
			return
		self.pos_order(root_node.l_child)
		self.pos_order(root_node.r_child)
		print(root_node.elem, end = '  ')

# use the stack
	def preoder(self, root_node):
		if root_node is None:
			return
		stack = []
		while root_node or len(stack):
			if root_node:
				stack.append(root_node)
				print(root_node.elem, end = '  ')
				root_node = root_node.l_child
			else:
				root_node = stack.pop()
				root_node = root_node.r_child

	def inoder(self, root_node):
		if root_node is None:
			return
		stack = []
		while root_node or len(stack):
			if root_node:
				stack.append(root_node)
				root_node = root_node.l_child
			else:
				root_node = stack.pop()
				print(root_node.elem, end = '  ')
				root_node = root_node.r_child

	def posorder(self, root_node):
		if root_node is None:
			return
		stack1 = []
		stack2 = []
		while root_node or len(stack1):
			if root_node:
				stack1.append(root_node)
				stack2.append(root_node.elem)
				root_node = root_node.r_child
			else:
				root_node = stack1.pop()
				root_node = root_node.l_child
		while stack2:
			print(stack2.pop(), end = '  ')

	def postOrder(self,root_node) :
		if not root_node :
			return
		stack = []
		stack.append(root_node)
		c = None
		while stack :
			c = stack [-1]
			if c.l_child and c.l_child != root_node and c.r_child != root_node :
				stack.append(c.l_child)
			elif c.r_child and c.r_child != root_node :
				stack.append(c.r_child)
			else :
				print(stack.pop().elem, end = ' ')
				root_node = c

	def morispre(self,root_node):
		if not root_node:
			return
		while root_node:
			cur = root_node.l_child
			if cur:
				while cur.r_child and cur.r_child is not root_node:
					cur = cur.r_child
				if not cur.r_child:
					cur.r_child = root_node
					print(root_node.elem, end = '  ')
					root_node = root_node.l_child
					continue
				else:
					cur.r_child = None
			else:
				print(root_node.elem, end = '  ')
			root_node = root_node.r_child

	def morisin(self,root_node):
		if not root_node:
			return
		while root_node:
			cur = root_node.l_child
			if cur:
				while cur.r_child and cur.r_child is not root_node:
					cur = cur.r_child
				if not cur.r_child:
					cur.r_child = root_node
					root_node = root_node.l_child
					continue
				else:
					cur.r_child = None
			print(root_node.elem, end = '  ')
			root_node = root_node.r_child

	def morispos(self,root_node):
		if not root_node:
			return

if __name__ == '__main__':
	tree = Tree()
	tree.__add__(0)
	tree.__add__(1)
	tree.__add__(2)
	tree.__add__(3)
	tree.__add__(4)
	tree.__add__(5)
	tree.__add__(6)
	tree.__add__(7)
	tree.__add__(8)
	tree.__add__(9)

	print('breath')
	tree.breath_travel()
	print('\npreorder')
	tree.pre_order(tree.root)
	print('\ninorder')
	tree.in_order(tree.root)
	print('\nposorder')
	tree.pos_order(tree.root)
	print('\nstack pre')
	tree.preoder(tree.root)
	print('\nstack in')
	tree.inoder(tree.root)
	print('\nstack pos')
	tree.posorder(tree.root)
	print('\nstack1 for pos order')
	tree.postOrder(tree.root)
	print('\nmorispre')
	tree.morispre(tree.root)
	print('\nmorisin')
	tree.morisin(tree.root)


