cities=[
]
n=1
city=str(input("enter your cities:\ncity:"))

while(city.lower() !="stop"):
    cities.append((city,len(city)*1000000))
    n+=1
    city=str(input(f"city {n}: "))
    
scities=sorted(cities,key=lambda x:x[1],reverse=True)
print(scities)