
fd = open('records.txt','r')

user = 780753555195
quantity = 5

products = fd.read().split("\n")

for product in products:

    if (int(product.split(",")[0]) == user):
        if (int(product.split(",")[3]) >= quantity):
            print(product.split(",")[1], "Book is available at Rs.",product.split(",")[2])
            print(product.split(",")[3])
        else:
            print(product.split(",")[1], "Book is available at Rs.",product.split(",")[2])
            print("There are ",product.split(",")[3],"books available")
#    print(product.split(","))


fd.close()
