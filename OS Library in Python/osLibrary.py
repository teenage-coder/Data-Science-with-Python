import os

print("OS Imported!")

print("Current Working Directory: ",os.getcwd())
print("List of all files at current Location: ",os.listdir())
print("List of all files at specific location: ",os.listdir("/Users/ashishjangra/Documents/Python/Lac 1"))

print("Crate a directory: ", os.mkdir("Hello"))

print("Crate multiple directory: ", os.makedirs("Hello/Hello1/Hello2/hello3"))

print("Remove directory: ", os.rmdir("Hello"))
