import functools
a=[]
b =[]
n = int(input('enter the no of element in the list'))
for i in range(n):
    element = int(input('enter the element you want to add'))
    a.append(element)
    
print('elements in the list :',a)
z = int(input('enter any no '))
print(z)
for i in a :
    if i<z:
        b.append(i)
print('elements in the new list are :',b)
