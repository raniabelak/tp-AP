width=int(input("the width of the line: "))
height=int(input("the height of the line: "))

for j in range(height):
    for i in range(width):
        print("#",end='') #end automatically is \n in print so derna '' to make sure it doesnt change line
    print("")
    
    
# we could have used print("#"*width)