# -*- coding: utf-8 -*-

def bubble_sort(alist):
	n  = len(alist)
	for i in range(n-1):
		print(alist)
		for j in range(n-i-1):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]

seq = [2,4,1,6,34,76,44,55]
bubble_sort(seq)

