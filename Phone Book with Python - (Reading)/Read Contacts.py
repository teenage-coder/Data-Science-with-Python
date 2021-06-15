fd = open("Phone Book.txt", 'r')

name = input("Enter name: ")

data = fd.read()
contacts = data.split('\n')

for contact in contacts:
    
    if(contact.split(",")[0].lower() == name.lower()):
        print("*****************")
        print("Name : ",contact.split(",")[0])
        print("Phone: ",contact.split(",")[1])
        print("*****************")

fd.close()



