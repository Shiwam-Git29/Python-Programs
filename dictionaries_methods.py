student ={
    "name":"Shivam",
    "city":"kolkata",
    "company":"meta"
}
student.pop("name")
print(student)

student.popitem()
print(student)

del student["name"]
print(student)

student.clear()
print(student)