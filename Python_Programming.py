#operators:
# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a//b)
# print(a**b)

#relational operators:
# a=10
# b=5
# print(a>b)
# print(a*a<100)
# print(a<b)
# print(a<=b)
# print(a>b)
# print(10==10)
# print(50!=60)
# print((10*20)!=(6*3))
# print((10*20)!=(20*10))
# print(10>=10)

# def checkevenodd(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# n=int(input("enter num:"))
# flag=checkevenodd(n)
# if flag==True:
#     print("EVEN")
# else:
#     print("FALSE")

# while True:
#     n=int(input("enter a value:"))
#     if n==5:
#         print("Hello World")
#         break
# print("prog exec")

#count digits
# n=int(input("enter num:"))
# c=0
# while n!=0:
#     n=n//10
#     c=c+1
# print(c)

# def count(n):
#     c=0
#     if n<0:
#         n=n*-1
#     while n !=0:
#         n=n//10
#         c+=1
#     return c
# n=int(input("enter a number:"))
# res=count(n)
# print(res)

# def count(n):
#     c=0
#     if n<0:
#         n=n*-1
#     while n !=0:
#         n=n//10
#         c+=1
#     return c
# st=int(input("enter a start number:"))
# en=int(input("enter a end number:"))
# for i in range(st,en+1):
#     res=count(i)
#     print("count of digits in",i,":",res)

# def count(n):
#     c=0
#     if n<0:
#         n=n*-1
#     while n !=0:
#         n=n//10
#         c+=1
#     return c
# st=int(input("enter a start number:"))
# en=int(input("enter a end number:"))
# if st>en:
#     print("Invalid range")
# else:
#     for i in range(st,en+1):
#         res=count(i)
#         print("count of digits in",i,":",res)

#reverse order:
# n=int(input("enter a number:"))
# rev=0
# if n<0:
#     n*=-1
# while n!=0:
#     rem=n%10
#     rev=(rev*10)+rem
#     n//=10
# print(rev)

#given number is integer palandrome number or not
# def checkpalindrome(n):
#     temp=n
#     rev=0
#     if n<0:
#         n=n*-1
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     if rev==temp:
#         return True
#     else:
#         return False
# n=int(input("enter a number:"))
# flag=checkpalindrome(n)
# if flag==True:
#     print("palandrome")
# else:
#     print("not a palandrome")

#armstrong number or not
# def countdigits(n):
#     c=0
#     while n!=0:
#         n//=10
#         c+=1
#     return c
# def checkasn(n):
#     c=countdigits(n)
#     temp=n
#     asn=0
#     while n!=0:
#         base=n%10
#         asn=asn+(base**c)
#         n//=10
#     return asn==temp
# n=int(input("enter a number:"))
# if checkasn(n):
#     print("ASN")
# else:
#     print("NOT A ASN")

#leepyear or not
# def leapyear(n):
#     if (n%100!=0 and n%4==0) or (n%400==0):
#         return True
#     return False
# n=int(input("enter a year"))
# flag=leapyear(n)
# if flag==True:
#     print("LEAP YEAR")
# else:
#      print("NOT A LEAPYEAR")

#recursive function
# def sumnn(n):
#     if n==1:
#         return 1
#     return n+sumnn(n-1)
# n=int(input("enter a number:"))
# res=sumnn(n)
# print(res)

#factorialnumber
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# n=int(input("enter a number:"))
# res=fact(n)
# print(res)

#sum of numbers
# def sum(n):
#     if n==0:
#         return 0
#     return (n%10)+sum(n//10)
# n=int(input("enter a number:"))
# res=sum(n)
# print(res)

#reverse the number
# def reverse(n, rev):
#     if n==0:
#         return rev
#     rev=(rev*10)+(n%10)
#     return reverse(n//10, rev)
# num=int(input("enter a number:"))
# res=reverse(num, 0)
# print(res)

#check panandrome or not:
# def palandrome(n,rev, temp):
#     if n == 0:
#         return rev==temp
#     rev = (rev * 10) + (n % 10)
#     return palandrome(n // 10, rev, temp)
# num = int(input("enter a number:"))
# res = palandrome(num, 0, num)
# print(res)

#print fibonacci series till the defind position
# def fibonacci(pos, n1, n2):
#     if pos==0:
#         return
#     print(n1,end=" ")
#     fibonacci(pos-1,n2,(n1+n2))
# num=int(input("enter position:"))
# fibonacci(num,0,1)

#write the program to check weather the given number is happy number or not
# def happynumber(n):
#     if n==1:
#         return True
#     if n==4:
#         return False
#     sum=0
#     while n!=0:
#         rem=n%10
#         sum=sum+(rem*2)
#         n//=10
#     return happynumber(sum)
# n=int(input("enter a number:"))
# if happynumber(n):
#     print("Happy Number")
# else:
#     print("Not A Happy Number")










