
print("***********************************")
print("Press 1 for searching the contact")
print("Press 2 for creating new contact")
print("***********************************")
choice = int(input("Enter your choice: "))


if (choice == 1):

    fd = open("Phone Book.txt", 'r')

    name = input("Enter the name: ")

    contacts = fd.read().split('\n')

    for i in contacts:
        if(i.split(",")[0].lower() == name.lower()):
            print(i)

    fd.close()

if (choice == 2):

    fd = open("Phone Book.txt", 'a')

    contact_name = input("Enter the name: ")
    contact_number = input("Enter the no: ")

    fd.write(contact_name)
    fd.write(",")
    fd.write(contact_number)
    fd.write("\n")

    print("")
    print("New Contact is created!")
    print("Name: ", contact_name)
    print("Phone: ", contact_number)

    fd.close()





