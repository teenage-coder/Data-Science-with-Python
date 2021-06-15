
dct = {1 : "John", 2 : "Joe" , 3 : "Jill" , 4 : "Jack" ,5 : "Johny"}


print("Get the value by key: ", dct[1])
print("Keys: ", dct.keys())
print("Keys: ", dct.values())


keys = dct.keys()

for roll_no in keys:
    print(roll_no , dct[roll_no])
