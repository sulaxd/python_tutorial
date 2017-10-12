size = 10
sample = []
count = []

print("Enter ten numbers:")

for i in range(size):
    num = eval(input())
    
    if num in sample:
        count[sample.index(num)] += 1
    else:
        count.append(1)
        
    sample.append(num)

num_occu = max(count)
print("Mode of the set: ", sample[count.index(num_occu)])
print("Number of occurrence: ", num_occu)