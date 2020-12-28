#Simple class and object with attributes and method
class Dog():
    speciec = 'Mammal'
    def __init__(self,myBreed,name):
        self.breed = myBreed
        self.name = name
    def bark(self):
        print("Woof!! My name is{}".format(self.name))

my_dog = Dog('Lab','Tommy')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.bark())


# Inheritance 
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an Animal")
    def eat(self):
        print("I am eating")

class Dogs(Animal):
    def __init__(self):
        super().__init__() # Animal.__init__(self)
        print("DOG CREATED")
    def who_am_i(self):
        super().who_am_i()
        print("I am a Dog")
    def eat(self):
        print("I am a dog and eating")
    def bark(self):
        print("WOOF !!!")

my_dog1 = Dogs()
print(my_dog1.eat())
print(my_dog1.who_am_i())
print(my_dog1.eat())
print(my_dog1.bark())