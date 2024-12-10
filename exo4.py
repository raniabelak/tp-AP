age1= int(input("enter the age of the first person: "))
age2= int(input("enter the age of the second person: "))

if(age1!= age2):
    max=max(age1, age2)
    print("the older age is:",max)
else:
    print("they are the same age!")