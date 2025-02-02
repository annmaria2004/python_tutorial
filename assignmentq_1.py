import functools
a=[10,11,23,52,67,89,12]
largest_no = functools.reduce(lambda x,y:x if x>y else y,a)
smallest_no = functools.reduce(lambda x,y:x if x<y else y,a)
print('Largest no in the list is',largest_no)
print('Smallest no in the list is',smallest_no)