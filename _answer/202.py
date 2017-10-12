a = int(input("Enter a number:"))

if a%3 == 0:
    print("%d is a multiple of 3." % a)
elif a%5 == 0:
    print("%d is a multiple of 5." % a)
else:
    print("%d is not a multiple of 3 or 5." % a)