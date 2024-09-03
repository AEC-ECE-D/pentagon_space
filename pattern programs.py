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

n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(i,end="")
        else:
            print(j,end="")
    print()






