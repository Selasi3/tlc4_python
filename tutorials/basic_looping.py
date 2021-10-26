print("Using the values from a tuple")
for i in {1,2,3,4,5}:
    print(i, " ", end='\n')
print("---------------------------------------------------")
print("Print out values in a range")
for i in range(1,10,2):
    print(i, " ",end="\n")
print("---------------------------------------------------")
print("Using break in a loop")
for i in range(1,10):
    if(i==6):
        break
    print(i, " ", sep=' ', end="\n")
print("done")
print("---------------------------------------------------")
print("Using break in a loop")
for i in range(1,10):
    if(i==6):
        continue
    print(i, " ", sep=' ', end="\n")
