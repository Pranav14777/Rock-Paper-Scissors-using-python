print("rock paper scissors account set up")
while true:
    username= input("enter your username")
    password=input("enter your password")
    conf_password=input("please confirm your password")
    if password!=conf_password:
        print("your passwords dont match")
    else:
        print("your account has been set up")
        text_file=open("access.csw","a")
        text_file.write(",")
        text_file.write(username)
        text_file.write(",")
        text_file.write(password)
        text_file.close()
        break 
