#Builder

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None
    
    def setBody(self, body):
        self._body = body
        
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)
        
    def setEngine(self,engine):
        self.__engine = engine
        
    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d" % self.__wheels[0].size)
        
        
#Car Parts

class Wheel:
    size = None
    
class Engine:
    horsepower = None
    
class Body:
    shape = None
    
    
class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
        
    # The Algorythm for assembling a car

    def getCar(self):
        car = Car()
        
        # Number 1 : Body

        body = self.__builder.getBody()
        car.setBody(body)

        # Number 2 : Engine

        engine = self.__builder.getEngine()
        car.setEngine(engine)
        
        # Number 3 : Wheels
        #Looping the 4 wheels
        
        i = 0
        while i<4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            
        return car    
    
#Builder Interface

class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass

#Different Complex Objects

class JeepBuilder(BuilderInterface):
    
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 600
        return engine
    
    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body
         
class ChevyBuilder(BuilderInterface):
    
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 30
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 300
        return engine
    
    def getBody(self):
        body = Body()
        bodi.shape = "Track"
        return body
         
d=Director()
print(d)        
print(d.setBuilder(JeepBuilder()))        
d.getCar()