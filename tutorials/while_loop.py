num = 0
while num < 10:
    if(num==6):
        break
    print(num, ' ', end=' ')
    num+=1
print("Done\n")
print("--------------------------------\n")
print("Repeating loop until test condition is false")
fx = 0 
x=0
while fx<500:
    fx = 2*x*(x+1)
    print(x, '\t: ', fx)
    x+=1
print("Done")