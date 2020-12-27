class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getShip(self):
        sheep = Sheep()

        body = self.__builder.getBody()
        sheep.setBody(body)

        engine = self.__builder.getEngine()
        sheep.attachEngine(engine)

        steps = self.__builder.getSteps()
        sheep.attachSteps(steps)

        fuel = self.__builder.getFuel()
        sheep.attachFuel(fuel)

        return sheep


class Sheep:
    def __init__(self):
        self.__engine = None
        self.__steps = None
        self.__fuel_compartments = None

    def setBody(self, body):
        self.__body = body

    def attachEngine(self, engine):
        self.__engine = engine

    def attachSteps(self, steps):
        self.__steps = steps

    def attachFuel(self, fuel):
        self.__fuel = fuel

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine power: %d" % self.__engine.power)
        print("count steps: %d" % self.__steps.count)
        print("count fuel compartments %d" % self.__fuel.fuel)


class Builder:
    def attachEngine(self): pass

    def attachSteps(self): pass

    def attachFuel(self): pass


class ShapeBuilder(Builder):

    def getEngine(self):
        engine = Engine()
        engine.power = 400
        return engine

    def getSteps(self):
        steps = Steps()
        steps.count = 4
        return steps

    def getBody(self):
        body = Body()
        body.shape = "CosmosShape"
        return body

    def getFuel(self):
        fuel = Fuel()
        fuel.fuel = 5
        return fuel


# Car parts
class Engine:
    size = None


class Steps:
    count = None


class Body:
    shape = None


class Fuel:
    fuel = None


shapeBuilder = ShapeBuilder()
director = Director()
# Build Jeep
print("Shape")
director.setBuilder(shapeBuilder)
shape = director.getShip()
shape.specification()
print("")
