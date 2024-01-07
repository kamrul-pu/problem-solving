# Defined class without any  class methods and variables


class Test:
    pass


# defining method variables
Test.x = 45

# defining class methods
Test.foo = lambda self: print("hello")

# creating object
myobj: Test = Test()
print(myobj.x)
myobj.foo()
