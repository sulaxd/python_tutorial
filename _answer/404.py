number = eval(input("Enter a positive integer: "))

print("The reversed number is: ", end = '')

if number == 0:
    print(number)
else:
    while number != 0:
        print(number%10, end = '')
        number //= 10