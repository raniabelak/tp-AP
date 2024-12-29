n = int(input("Enter a positive integer: "))
while n <= 0:
    print("Please enter a positive integer.")
    n = int(input("Enter a positive integer: "))

for i in range(-n, n + 1):
    if i != 0:
        print(i)
