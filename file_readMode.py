file=open("robot.txt","r")
content = file.readline() #"it's a also a print same things of your robot file but it excess all words as a string"
content = file.read()
print(content)

file.close()