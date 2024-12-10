print("runner1:")
name1=str(input("name: "))
time1=float(input("time (in seconds): "))

print("runner2:")
name2=str(input("name: "))
time2=float(input("time (in seconds): "))

if(time1==time2): 
    print(name1,"and",name2,"have the same time")
else:
    min=min(time1,time2)
    if(min==time1): 
        print(name1,"is the fastest runner")
    else:
        print(name2,"is the fastest runner")