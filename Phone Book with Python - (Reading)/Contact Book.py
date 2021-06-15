fd = open("Phone Book.txt", 'a')

name = input("Enter name: ")
phone = input("Enter phone no: ")

fd.write(name)
fd.write(",")
fd.write(phone)
fd.write("\n")

fd.close()
