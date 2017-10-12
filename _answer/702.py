tup1 = ()
tup2 = ()

print("Creat tuple1:")
while True:
    num = eval(input())
    if num == -9999: break
    tup1 += (num,)

print("Creat tuple2:")
while True:
    num = eval(input())
    if num == -9999: break    
    tup2 += (num,)
    
tup_comb = tup1 + tup2

print("Combined tuple before sorting:", tup_comb)

lst_comb = list(tup_comb)
print("Combined tuple after sorting:", sorted(lst_comb))