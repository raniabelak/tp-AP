

amount= float(input("total amount: "))
items=int(input("number of items: "))
day=str(input("day of the week: "))


if(day.lower()in{"saturday","sunday" }):
    discharge=0.2
elif(day.lower()in{"monday","tuesday","wednesday","thursday","friday"}):
    discharge=0.1
else:
    print("invalid day")
    exit()

if(items>5):
    discharge=discharge+0.05
    
price=amount-amount*discharge
print("price after discharge is:",price,"DA")