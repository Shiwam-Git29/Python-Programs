student ={
    "name":"Shivam",
    "city":"kolkata",
    "company":"meta"
}

print(student.keys())

print(student.values())

print(student.items())

for keys in student:
    print(keys)

for values in student:
    print(values)

for keys, values in student.items():
    print(keys,values)    
    