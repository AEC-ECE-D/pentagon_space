str=input("enter a string:")
newstr=""
i=0
while(i<=len(str)-1):
    char=str[i]
    ascii=ord(char)
    if ascii>=65 and ascii<=90:
         newascii=ascii+32
         conchar=chr(newascii)
         newstr=newstr+conchar
    else:
         newstr=newstr+char
    i=i+1
print(newstr)


