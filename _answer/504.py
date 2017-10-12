def compute(a, b):
    return a**b

a = eval(input("Enter a number: "))
b = eval(input("Enter power of number: "))

print(a, '^', b, '=', compute(a, b))