total = 0
string = input("Enter a String: ")

for i in range(0,len(string)):
    num = ord(string[i])
    print("ASCII code for '%s' is %d" % (string[i], num))
    total += num
    
print("Sum = ", total)