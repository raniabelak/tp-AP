numbers = [1, 2, 3, 4, 5]
print(numbers)
print("Menu: \n1.Append\n2.Insert\n3.Pop\n4.Remove\n5.Sort\n6.Reverse\n7.Search\n8.Save to file\n9.Quit")

a = int(input("Choose an option: "))
while a != 9:
    if a == 1:
        numbers.append(int(input("Enter value: ")))
    elif a == 2:
        b = int(input("Enter index: "))
        if b < len(numbers):
            numbers.insert(b, int(input("Enter value: ")))
    elif a == 3:
        if numbers:
            numbers.pop()
        else:
            print("List is empty. Nothing to pop.")
    elif a == 4:
        b = int(input("Enter index to remove: "))
        if 0 <= b < len(numbers):
            numbers.pop(b)
        else:
            print("Invalid index.")
    elif a == 5:
        numbers.sort()
    elif a == 6:
        numbers.reverse()
    elif a == 7:
        b = int(input("Enter value: "))
        if b in numbers:
            print("Value found at index", numbers.index(b))
        else:
            print("Value not found.")
    elif a == 8:
        filename = input("Enter filename to save: ")
        with open(filename, 'a') as file:  # Append mode to add data
            file.write(str(numbers) + '\n')
        print("List appended to", filename)
    elif a == 9:
        break
    else:
        print("Invalid option. Please choose a valid number.")

    print(numbers)
    a = int(input("Choose an option: "))

print("Program exited.")
