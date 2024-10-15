# n=int(input("enter a number:"))
# for i in range(n):
#     print("*")

# n=int(input("enter a number:"))
# for i in range(n):
#     print("*",end=" ")

# n=int(input("enter a number:"))
# for i in range(n):
#     print("* "*n)

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print("* "*i)

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print("  ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print("  ",end="")
#     for j in range(n,i-1,-1):
#         print("* ",end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end="")
#     for j in range(n,i-1,-1):
#         print("* ",end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(j,end=" ")
#     print()

# n=int(input("enter a number:"))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

# n=int(input("enter a number:"))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1

# n=int(input("enter a number:"))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

# n=int(input("enter a number:"))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1

# n=int(input("enter a number:"))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print(j,end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1

# n=int(input("enter a number:"))
# noc=1
# nor=(n*2)-1
# for i in range(1,(n*2)):
#     for j in range(1,(n*2)):
#         if j<= noc or j>=nor:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(j,end="")
#         else:
#             print(i,end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(i,end="")
#         else:
#             print(j,end="")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(i,end="")
#         else:
#             print(j,end="")
#     print()


# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>j:
#             print(j,end="")
#         else:
#             print(i,end="")
#     print()

# n=int(input("enter a number:"))
# odd=1
# for i in range(1,n+1):
#     for k in range(n,i-1,-1):
#         print(" ",end=" ")
#     for j in range(1,odd+1):
#         print("*",end=" ")
#     print()
#     odd+=2

# n=int(input("enter a number:"))
# c=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(c,end=" ")
#         c+=1
#     print()

# n=int(input("enter a number:"))
# c1=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2!=0:
#             print(c1,end=" ")
#             c2=c1
#         else:
#             print(c2, end=" ")
#             c2-=1
#         c1+=1
#     print()
#     c2=c2+n

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

# n=int(input("enter a number:"))
# c=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(96+c),end=" ")
#         c+=1
#     print()

# n=int(input("enter a number:"))
# c=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if c%2!=0:
#             print(chr(64+c),end=" ")
#         else:
#             print(chr(96+c),end=" ")
#         c+=1
#     print()

# n=int(input("enter a number:"))
# c=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if c%2==0:
#             print(chr(96+c),end=" ")
#         else:
#             print(chr(64 + c), end=" ")
#         c+=1
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print("-", end=" ")
#     print()

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==j or i+j==n+1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print("-", end=" ")
#     print()













