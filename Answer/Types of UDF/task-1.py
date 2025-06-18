def create_lists():
    number_lists = int(input("Enter the number of lists: "))
    all_lists = []

    for i in range(number_lists):
        # print(f"\nList {i + 1}:")
        n = int(input(f"\nEnter number of elements in list {i + 1}: "))
        current_list = []
        for j in range(n):
            element_add = int(input(f"Enter element {j + 1}: "))
            current_list.append(element_add)
        all_lists.append(current_list)

    return all_lists

result = create_lists()


print("\nAll Lists:")
i = 1
for ls in result:
    print("List", i, ":", ls)
    i += 1





































