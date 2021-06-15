import os


for i in range(1,6):

    os.mkdir("Level A/Level B " + str(i))
    
    print("Level A/Level B " + str(i))

    for j in range(1,6):

        os.mkdir("Level A/Level B " + str(i) + "/Level C " + str(j))
        print("Level A/Level B " + str(i) + "/Level C " + str(j))

        
