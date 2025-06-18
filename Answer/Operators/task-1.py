ls = []
n = int(input("Enter number of elements: "))


for i in range(n):
    element = int(input("Enter element " + str(i + 1) + ": "))
    ls.append(element)

print("\nCreated list:", ls)
print("Total sum of list:", sum(ls))
