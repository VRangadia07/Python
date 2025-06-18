def calculate(ls1, ls2, ls3):
    print("\nList ls1:", ls1)
    print("Sum of ls1:", sum(ls1))
    print("\nList ls2:", ls2)
    print("Sum of ls2:", sum(ls2))
    print("\nList ls3:", ls3)
    print("Sum of ls3:", sum(ls3))
    
    concate_list = ls1 + ls2 + ls3
    print("\nConcatenate List: ", concate_list)
    
    total_of_sum = sum(concate_list)
    print("Sum of all elements:", total_of_sum)
 

def create_list():
    num_list = int(input("Enter the number of lists: "))
    all_list = []
    
    for i in range(num_list):
        n = int(input(f"\nEnter number of elements in list {i + 1}: "))
        current_list = []
        for j in range(n):
            element_add = int(input(f"Enter element {j + 1}: "))
            current_list.append(element_add)
        all_list.append(current_list)
        
    return all_list

list = create_list()
calculate(list[0], list[1], list[2])