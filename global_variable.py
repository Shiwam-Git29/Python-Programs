x= 78 #global variable
def show_values():
    global x
    x=45
    print(x)
show_values() 
show_values() 
print(x)  