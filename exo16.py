numbers=[1, 2, 3, 4, 5]


a=int(input("Enter index: (-1 to quit)"))
while(a!=-1):
    if(a>=len(numbers) or a<0):
        print("Invalid index")
        exit()
    else:
        b=int(input("Enter value:"))
        numbers[a]=b
        print(numbers)
        a=int(input("Enter index: (-1 to quit)"))