#Abstract shape classes
class Shape2DInterface:
    def draw(self): pass

class Shape3DInterface:
    def build(self): pass
    
#Concrete shape classes
class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")
        
class Square(Shape2DInterface):
    def draw(self):
        print("Square.draw")

class Sphere(Shape3DInterface):
    def build(self):
        print("Sphere.build")

class Cube(Shape3DInterface):
    def build(self):
        print("Cube.build")

        
#Abstract Shape Factory
class ShapeFactoryInterface:
    def getShape(sides): pass
    

#Concrete Shape Factory
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Not a 2D shape creation: shape not defined for "+ sides + "sides"
        
class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        ''' Sides instead of faces'''
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, "Not a 3D shape creation: shape not defined for "+ sides + "faces "

        
s2 = Shape2DFactory()
s2.getShape(1)
s2.getShape(4).draw()
s3= Shape3DFactory()
s3.getShape(1)
s3.getShape(6).build()