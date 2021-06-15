
fd = open('records.txt','r')

user = 780753555195
quantity = 40

products = fd.read().split("\n")

updated = []

for product in products:

    if (int(product.split(",")[0]) == user):         # Check if product exists
        
        if (int(product.split(",")[3]) >= quantity): # Check the units/quantity
            
            print(product.split(",")[1], "Book is available at Rs.",product.split(",")[2])
            print("You'r billing amount is Rs.",int(product.split(",")[2])*quantity)

            temp = product.split(",")[0] +","+ product.split(",")[1] +","+ product.split(",")[2] + ","+str(int(product.split(",")[3]) - quantity)
            updated.append(temp)

            
        else:
            print("We are having ",product.split(",")[3],"book available")


    else:
        updated.append(product)

fd.close()
print("****************************")


fd = open('records.txt','w')


for i in updated:
    
    fd.write(i)
    fd.write("\n")

fd.close()

















