ls = [1, 2, 3, "11", ['a', 'b', 'c'], 4, 5, 6,
      ['d', 'e', 'f'], 7, 'g', 8, 'h',
      [9, 10, 'i', 'j'], 11, 'aansh']

for item in ls:
    if type(item) == list:
        for sub_item in item:
            print("\t" + str(sub_item))
    elif item in ['g', 'h']:  
        print("\t" + str(item))
        if item == 'h':
            break
    else:
        print(item)











# ls = [1, 2, 3, "11", ['a', 'b', 'c'], 4, 5, 6,
#       ['d', 'e', 'f'], 7, 'g', 8, 'h',
#       [9, 10, 'i', 'j'], 11, 'aansh']

# for item in ls:
#     if type(item) == list:
#         for sub_item in item:
#             print("\t" + str(sub_item)) 
#     else:
#         print(item)
#         if item == 'h':
#             break







# ls = [1, 2, 3, "11", ['a', 'b', 'c'], 4, 5, 6,
#       ['d', 'e', 'f'], 7, 'g', 8, 'h',
#       [9, 10, 'i', 'j'], 11, 'aansh']

# for item in ls:
#     if type(item) == list:
#         for sub_item in item:
#             print("\t" + str(sub_item))  
#     else:
#         print(item)

