lst = [12 ,13, 14, 15, 12, 32, 34, 54, 68, 34, 32, 33, 99 , 99 ,99]

subm = 0

for i in lst:
    subm = subm + i


print(subm / len(lst))
print(sum(lst) / len(lst))
