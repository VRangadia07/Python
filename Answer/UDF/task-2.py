def char_interchange(ls, i, j):
    
    char_list = list(ls)

    
    char_list[i], char_list[j] = char_list[j], char_list[i]

    return ''.join(char_list)

ls = input("Enter a string: ")
i = int(input("Enter the first index to interchange: "))
j = int(input("Enter the second index to interchange: "))


if i < 0 or j < 0 or i >= len(ls) or j >= len(ls):
    print("Invalid index positions.")
else:
    
    result = char_interchange(ls, i, j)
    print("String after interchange:", result)
