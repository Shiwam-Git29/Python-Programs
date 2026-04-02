a="heyy\n i'm harry!"
with open("harry.txt","a") as file: #"if you are using with keyword so you dont need to wtite file.close after open the file it can be also and automatically"
    file.write(a)
