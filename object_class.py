class student:
    def __init__(self):
        self.name="vivek"
        self.age=22
        self.height=5.6
        self.address="hyderabad"
    def dance(self):
        print("vivek is dancing")
    def study(self):
        print("vivek is studying")
s1=student()
print(s1.name)
print(s1.age)
print(s1.height)
print(s1.address)
s1.dance()
s1.study()
print("===============================================")
s1.age=23
print(s1.name)
print(s1.age)
print(s1.height)
print(s1.address)
s1.dance()
s1.study()

print("===============================================")
class hero:
    def __init__(self):
        self.name="Mahesh"
        self.age="48"
        self.height=6.2
    def dance(self):
        print("hero is dancing")
    def fight(self):
        print("hero is fighting")
h1=hero()
print(h1.name)
print(h1.age)
print(h1.height)
h1.dance()
h1.fight()
print("==============================================")
h2=h1
h2.name="yash"
print(h2.name)
print(h2.age)
print(h2.height)
h2.dance()
h2.fight()

print("=============================================== ")
print(h1) #address
print(id(h1)) #id of address


