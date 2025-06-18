num = int(input("Enter a number: "))

factorial = 1
i = 1

if num < 0:
    print("Factorial is not for negative numbers.")
else:
    while i <= num:
        factorial *= i
        i += 1

    print(f"Factorial of {num} is: {factorial}")
