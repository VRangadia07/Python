def calculate(*lists):
    print("\nList of sums:")
    i = 1
    for lst in lists:
        print(f"ls{i} sum is: {sum(lst)}")
        i += 1
        
    
    concate_list = [item for lst in lists for item in lst]
    print("\nConcatenated List:", concate_list)
    
    square_list = list(map(lambda x: x**2, concate_list))
    print("Squares of all elements:", square_list)
    
    odd_list = list(filter(lambda x: x % 2 != 0, concate_list))
    print("Odd Numbers:", odd_list)
    
    

num_list = int(input("Enter the number of lists: "))
all_lists = []

for i in range(num_list):
    n = int(input(f"\nEnter numbers of elements in list {i + 1}: "))
    current_list = []
    for j in range(n):
        element_add = int(input(f"Enter element {j + 1} of list {i + 1}: "))
        current_list.append(element_add)
    all_lists.append(current_list)

calculate(*all_lists)
    
    
























    