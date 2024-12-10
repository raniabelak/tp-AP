need= int(input("how many people needs a ride"))

fit = int(input("how many people fits in one taxi?"))

a = need / fit

if a - int(a) == 0:
    print("you need", int(a), "taxi")
else:
    print("you need", int(a)+1, "taxi")