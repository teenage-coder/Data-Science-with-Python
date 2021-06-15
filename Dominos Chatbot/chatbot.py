import time

print("Hello! Welcome to Dominos!")

print("What kind of pizza do you want?")
print("")
print("---------------------")
print("  1 for Veg Pizza")
print(" 2 for Non-Veg Pizza")
print("---------------------")


veg_or_non = int(input("Press your choice: "))

print("\n\n")
print("---------------------")
print("Dominos Veg Pizza Menu")
print("---------------------")
print(" 1. ExtraVagenza")
print(" 2. Cloud-9")
print(" 3. Deluxe Veggoe")
print(" 4. Paneer")
print(" 5. 5 Pepper")
print("---------------------")


pizza_name = int(input("Press your choice: "))


print("\n\n")
print("---------------------")
print(" 1. Regular")
print(" 2. Medium")
print(" 3. Large")
print("---------------------")

pizza_size = int(input("Press your choice: "))

quantity = int(input("How many: "))


pizza = {   1: {'name':"ExtraVagenza", 'regular' : 300, 'medium' : 500, 'large' : 800},
            2: {'name':"Cloud-9" ,'regular' : 300, 'medium' : 500, 'large' : 800},
            3: {'name':"Deluxe Veggie" ,'regular' : 300, 'medium' : 500, 'large' : 800},
            4: {'name':"Paneer" ,'regular' : 300, 'medium' : 500, 'large' : 800},
            5: {'name':"5 Pepper" ,'regular' : 300, 'medium' : 500, 'large' : 800},}

size = {1 : "regular", 2 : 'medium', 3 : 'large'}



print("Pizza Name: ",pizza[pizza_name]['name'])
print("Size: ", size[pizza_size])
print("Price: ", pizza[pizza_name][size[pizza_size]])
print("Quantities: ", quantity)
print("Billing Amount: ",pizza[pizza_name][size[pizza_size]] * quantity)


name     = pizza[pizza_name]['name']
s        = size[pizza_size]
price    = pizza[pizza_name][size[pizza_size]]
quantity = quantity
bill     = pizza[pizza_name][size[pizza_size]] * quantity


txt = name + ',' + s + ',' + str(price) + ',' + str(quantity) + ',' + str(bill) + "," +time.ctime() + '\n'

fd = open("record.txt",'a')

fd.write(txt)

fd.close()