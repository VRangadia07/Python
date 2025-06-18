a = input("Enter variable values: ")  # e.g. 1,a,2,b,3,4,55,asit,nimesh

items = a.split(',')

int_list = []
str_list = []

for item in items:
    if item.isdigit():
        int_list.append(int(item))  
    else:
        str_list.append(item)       

print("\nInteger List:", int_list)
print("Min:", min(int_list))
print("Max:", max(int_list))

reversed_strings = []
for s in str_list:
    reversed_s = s[::-1]
    reversed_strings.append(reversed_s)
# reversed_strings = [s[::-1] for s in str_list]

print("\nString List:", str_list)
print("Reversed Strings:", reversed_strings)




# a = input("Enter values: ") 

# str_list = []
# int_list = []

# items = a.split(',')

# for item in items:
#     if item.isdigit():
#         int_list.append(int(item))
#     else:
#         str_list.append(item)

# print("Integer list:", int_list)
# print("Minimum:", min(int_list))
# print("Maximum:", max(int_list))

# print("Original string list:", str_list)
# print("Reversed strings:")
# for s in str_list:
#     print(s[::-1])
