a =[]
b=[]
n = int(input('Enter the no of elements in the list\n'))
for i in range(n):
    element= int(input('enter the element you want to add'))
    a.append(element)
print('elements in the list are:',a)

for i in a:
    if i%2==0:
        b.append(i)
print('list containing only even elements :',b)