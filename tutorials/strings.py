x = "Good"
y = " day"
result = x+y
#String concatenation
print(result)
print("type: ", (type(result)))
print("length of string: ", len(result))
print("Upper case: ", result.upper())
print("Lower case: ", result.lower())
print("Title: ", result.title())
print("Count the occurrence of o: ", result.count("o"))

print("-----------------------------")
print("Spliting a string")
b=result.split(sep=" ")
print(b)