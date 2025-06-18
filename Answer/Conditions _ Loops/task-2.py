num = int(input("Enter a number: "))


int_constant = 3
float_constant = 1.5

if num >= 0:
    if num % 2 == 0:
        result = num * float_constant
        print(f"Positive even: {num} * {float_constant} = {result}")
    else:
        result = num + int_constant
        print(f"Positive odd: {num} + {int_constant} = {result}")
else:
    if num % 2 == 0:
        result = num / float_constant
        print(f"Negative even: {num} / {float_constant} = {result}")
    else:
        result = num - int_constant
        print(f"Negative odd: {num} - {int_constant} = {result}")



















# num = int(input("Enter a number: "))

# 
# int_constant = int(input("Enter an integer constant: "))
# float_constant = float(input("Enter a floating-point constant: "))

# 
# if num >= 0:
#     if num % 2 == 0:
#         result = num * float_constant
#         print(f"Positive even: {num} * {float_constant} = {result}")
#     else:
#         result = num + int_constant
#         print(f"Positive odd: {num} + {int_constant} = {result}")
# else:
#     if num % 2 == 0:
#         result = num / float_constant
#         print(f"Negative even: {num} / {float_constant} = {result}")
#     else:
#         result = num - int_constant
#         print(f"Negative odd: {num} - {int_constant} = {result}")
