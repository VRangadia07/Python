n = int(input("Enter number of elements: "))  
ls = []


for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))  
    ls.append(element) 


for i in range(1, n):  
    ls1 = ls[:i]  
    ls2 = ls[i:]  

    if sum(ls1) == sum(ls2):  
        print("\nFound equal sum sublists:")
        print("ls1 =", ls1, "=>", sum(ls1))
        print("ls2 =", ls2, "=>", sum(ls2))
        break  


else:
    print("\nNo found sublists.")



