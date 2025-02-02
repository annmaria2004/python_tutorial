a = []
b = []
c = []
n = int(input('enter the no of elements in the list '))
for i in range(n):
    element = int(input('enter the elements to add'))
    a.append(element)
print('elements in a are :',a)
for i in range(n):
    element = int(input('enter the elements to add'))
    b.append(element)
print('elements in b are :',b)
for i in a :
    for j in b:
        if i==j:
            c.append(i)
print('elements that are common in both list are :',c)

