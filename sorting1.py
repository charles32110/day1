# -*- coding: utf-8 -*-

def bubble_sort(alist):
	n  = len(alist)
	for i in range(n-1):
		print(alist)
		for j in range(n-i-1):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]

seq = [2,4,1,6,34,76,44,55]
# bubble_sort(seq)

def selected_sort(seq):
	n = len(seq)
	for i in range(n -1):
		min = i
		for j in range(i+1,n):
			if seq[j] < seq[min]:
				min = j
		if min != i:
			seq[i], seq[min] = seq[min],seq[i]


# selected_sort(seq)


def insert_sort(seq):
	n = len(seq)
	for i in range(1,n):
		value = seq[i]
		pos = i
		while pos > 0 and value < seq[pos-1]:
			seq[pos] = seq[pos-1]
			pos -= 1
		seq[pos] = value
		print(seq)

def shell_sort(alist):

	n = len(alist)
	gap = n // 2
	while gap >= 1:
		for j in range(gap, n):
			i = j
			while (i - gap) >= 0:
				if alist[i] < alist[i - gap]:
					alist[i], alist[i - gap] = alist[i - gap], alist[i]
					i -= gap
				else:
					break
		gap //= 2

def merge_sort(seq):
	n  = len(seq)
	if n <= 1:
		return seq
	mid = n // 2
	seq_left = merge_sort(seq[:mid])
	seq_right = merge_sort(seq[mid:])
	return merge(seq_left,seq_right)

def merge(left,right):
	left_len , right_len = len(left), len(right)
	left_point , right_point = 0, 0
	result = list()
	while left_point< left_len and right_point <right_len:
		if left[left_point] >= right[right_point]:
			result.append(right[right_point])
			right_point += 1
		else:
			result.append(left[left_point])
			left_point += 1

	result += left[left_point:]
	result += right[right_point:]
	return result

def quick_sort(seq):
	if len(seq) < 2:
		return seq
	pivot_index = 0
	pivot = seq[pivot_index]
	less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
	more_part = [i for i in seq[pivot_index+1:] if i > pivot]
	return quick_sort(less_part) + [pivot] + quick_sort(more_part)

alist = [54, 26, 93, 17, 77]
print(quick_sort(alist))
