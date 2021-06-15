
fd = open('records.txt','r')

data = fd.read()

lines = data.split(".")


print(len(lines) - 1)
print(lines)

fd.close()
