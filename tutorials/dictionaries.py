d ={"one":1, "two":2}
print("d:", d)
print("Type: ",type(d))
print("add a new key,value to the dictionary d")
d['three'] =3 
print("d: ", d)
print("remove a  key,value from the dictionary d")
del d["two"]
print("d: ", d)
print("----------------------------------------")
seasons = {"Spring":("Mar", "Apr", "May"),
            "Winter": ("Dec","Jan","Feb")}
print("Spring seasons: ", seasons["Spring"])
print("2nd month in Spring seasons: ", seasons["Spring"][1])
print("keys of Seasons")
print(seasons.keys())
print("values of Seasons")
print(seasons.values())

values = seasons.values()
for i in values:
    print(i)
print("----------------------------------------")
print("using items() to return key, value pairs")
print(seasons.items())
print("----------------------------------------")
print("Sorting keys")
print(sorted(seasons.keys()))