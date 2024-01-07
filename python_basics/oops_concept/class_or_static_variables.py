# Python program to show that the variables with a value
# assigned in class declaration, are class variables


# Class for Computer Science Student
class CSStudent:
    stream = "cse"  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


# Objects of CSStudent class
a = CSStudent("Geek", 1)
b = CSStudent("Nerd", 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = "ece"
print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = "mech"

print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'mech'


class MyClass:
    static_var = 0

    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var


obj1 = MyClass()
print(obj1.instance_var)  # Output: 1

obj2 = MyClass()
print(obj2.instance_var)  # Output: 2

print(MyClass.static_var)  # Output: 2
