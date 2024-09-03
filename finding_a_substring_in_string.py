# str="if you think you can or you can't then you are right"
# print(str.find("you"))
# print(str.rfind("you"))

str=input("enter a string value=")
if (str.isalpha()):
    print("str contains only characters")
elif (str.isnumeric()):
    print("str contains only numbers")
elif (str.isalnum()):
    print("str contains only characters and numbers")
