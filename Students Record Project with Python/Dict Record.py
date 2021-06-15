record = { 1 : {"Name" : "John"  , "Class" : 9, "Eng" : 92 , "Sci" : 76, "Math" : 87},
           2 : {"Name" : "Joe"   , "Class" : 4, "Eng" : 62 , "Sci" : 76, "Math" : 87} ,
           3 : {"Name" : "Jill"  , "Class" : 6, "Eng" : 72 , "Sci" : 76, "Math" : 87},
           4 : {"Name" : "Jack"  , "Class" : 7, "Eng" : 96 , "Sci" : 76, "Math" : 87},
           5 : {"Name" : "Johny" , "Class" : 10, "Eng" : 84 , "Sci" : 76, "Math" : 87}}


for roll_no in record.keys():
    print(record[roll_no]["Name"])

    if (record[roll_no]["Name"] == "John"):
        print("Student Found!")
        break
    
lst = ['John', 'Joe', 'Jill', 'Jack',' Johny']

for i in lst:
    if (i == 'John'):
        print("Student Found")
        break
