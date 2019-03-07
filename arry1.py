# -*- coding: utf-8 -*-

"""array"""




class Array(object) :
	'''text'''

	def __init__(self) :
		self.item = None

	def __getitem__(self,index):
		return self.item[index]

	def __setitem__(self, index, value):
		self.item[index] = value

	def __len__(self):
		return len(self)

	def iter(self):
		for item in self.item:
			yield item




