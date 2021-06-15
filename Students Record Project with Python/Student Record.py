
record = { 1 : {"Name" : "John"  , "Class" : 9, "Eng" : 92 , "Sci" : 76, "Math" : 87},
           2 : {"Name" : "Joe"   , "Class" : 4, "Eng" : 62 , "Sci" : 76, "Math" : 87} ,
           3 : {"Name" : "Jill"  , "Class" : 6, "Eng" : 72 , "Sci" : 76, "Math" : 87},
           4 : {"Name" : "Jack"  , "Class" : 7, "Eng" : 96 , "Sci" : 76, "Math" : 87},
           5 : {"Name" : "Johny" , "Class" : 10, "Eng" : 84 , "Sci" : 76, "Math" : 87}}

roll_no = int(input("Enter the roll no: "))
student = record[roll_no]

print("**********************")
print("Name: " , student["Name"])
print("Class: ", student["Class"])
print("English Marks : ", student["Eng"])
print("Science Marks : ",student["Sci"])
print("Math Marks : ",student["Math"])

print("Average Marks: ", ( student["Eng"] + student["Sci"] + student["Math"] ) / 3)

print("**********************")


