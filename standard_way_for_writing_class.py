class student:
    def __init__(self,n,a,h,ad):
        self.name=n
        self.age=a
        self.height=h
        self.address=ad
    def study(self):
        print("student is studying")
s1=student("vivek",22,5.8,"hyderabad")
s2=student("prasanna",22,6.1,"hyderabad")
print(s1.name)
print(s2.name)
print(s1.address)
print(s2.address)

