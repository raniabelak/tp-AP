year=int(input("type a year: "))

leap=False

if(year%100 == 0):
    if(year%400 == 0):
        leap=True
elif(year%4==0):
    leap=True


if(leap==False):
    print("it's not a leap year")
else:
    print("it's a leap year")