# read annual income from user
income = int(input("Enter annual income:\n"))
tax=0
cess =0
total_tax=0

if income<=300000:
    tax = 0
if income<=600000:
    tax = (income-300000)*0.05
    cess = 0.04*tax
    total_tax = tax+cess
    
elif income<=900000:
    tax = (income-600000)*0.1+300000*0.05
    cess = 0.04*tax
    total_tax = tax+cess
    
elif income<=1200000:
    tax = (income-900000)*0.15+300000*0.05+300000*0.1
    cess = 0.04*tax
    total_tax = tax+cess
    
elif income<=1500000:
    tax = (income-1200000)*0.2+300000*0.05+300000*0.1+300000*0.15
    cess = 0.04*tax
    total_tax = tax+cess
    
elif income>1500000:
    tax = (income-1500000)*0.3+300000*0.05+300000*0.1+300000*0.15+300000*0.2
    cess = 0.04*tax
    total_tax = tax+cess
    
print("Income Tax:",total_tax)
    