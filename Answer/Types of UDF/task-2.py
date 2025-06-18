def calculate(ls1, ls2):
    print("\nls1:", ls1)
    print("Sum of ls1:", sum(ls1))
    
    print("\nls2:", ls2)



def create_list():
    num_list = int(input("Enter the number of lists: "))
    all_lists = []
    
    for i in range(num_list):
        n = int(input(f"\nEnter number of elements in list {i + 1}: "))
        current_list = []
        for j in range(n):
            element_add = int(input(f"Enter element {j + 1}: "))
            current_list.append(element_add)
        all_lists.append(current_list)
             
    return all_lists



list = create_list()


if len(list) >= 2:
    calculate(list[0], list[1])

