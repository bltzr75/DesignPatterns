#Inheritance

class Pet(object):
    def __init__(self, name, species):
        self.name=name
        self.species=species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def __str__(self):
        return "%s is a %s" % (self.name,self.species)
    
    
d = Pet("Dorkly", "Monkey")
print(d.name)
print(d.species)
print((d).__str__())
    
       
    
class Dog(Pet):
    
    def __init__(self, name, chases_cats):
        super().__init__(name,"Dog")
        self.chases_cats = chases_cats
        
    def chasesCats(self):
        return self.chases_cats
    
    def __str__(self):
        additional_info = ""
        if self.chases_cats:
            additional_info = " who chases cats"
        return super().__str__() + additional_info

b = Dog("Bully",True)
b.__str__()
print(Dog.__bases__)
print(Pet.__bases__)
Pet.__subclasses__()

#Multiple Inheritance


class A(object):
    def __init__(self):
        print("A")

    @staticmethod
    def foo():
        print("foo")

class B(object):
    def __init__(self):
        print("B")
    
    @staticmethod
    def bar():
        print("bar")
        
class C(A,B):
    def foobar(self):
        self.foo()
        self.bar()

print(" Multiple Resolution Order: ")        
print(C.__mro__)  
C.foo()
C.bar()
c=C()
c.foobar()