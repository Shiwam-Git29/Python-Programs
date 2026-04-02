items = ["apple", "banana" ,"grapes", "cucumber"]
print(len(items))

items.append("pineapple")
print(items)

items.insert(1 , "milk")
print(items)

items.extend(["more bananas and more grapes"])
print(items)  

items.remove("apple")
print(items)

items.pop()
print(items)

items.clear()
print(items)

print(items.index ("apple"))

