class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getShip(self):
        sheep = Sheep()

        # First goes the body
        body = self.__builder.getBody()
        sheep.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        sheep.attachEngine(engine)

        # And four wheels

        steps = self.__builder.getSteps()
        sheep.attachSteps(steps)


        return sheep


# The whole product
class Sheep:
    def __init__(self):
        self.__engine = None
        self.__steps = None
        self.__fuel_compartments = None
        self.__equipment = None

    def setBody(self, body):
        self.__body = body

    def attachEngine(self, engine):
        self.__engine = engine

    def attachSteps(self, steps):
        self.__steps = steps

    def setFuel_compartments(self, fuel_compartments):
        self.__fuel_compartments = fuel_compartments

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine power: %d" % self.__engine.power)
        print("count steps: %d" % self.__steps.count)



class Builder:
    def attachEngine(self): pass

    def attachSteps(self): pass

    def setFuel_compartments(self): pass


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

    def getFuelcompartments(self):
        fuel_compartments = FuelCompartments()
        fuel_compartments.fuel = "5топлвныхотсеков"
        return fuel_compartments


# Car parts
class Engine:
    size = None

class Steps:
    count = None

class Body:
    shape = None

class FuelCompartments:
    fuel = None


shapeBuilder = ShapeBuilder()
director = Director()
# Build Jeep
print("Shape")
director.setBuilder(shapeBuilder)
shape = director.getShip()
shape.specification()
print("")
