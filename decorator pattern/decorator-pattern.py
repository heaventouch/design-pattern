class Beverage(object):
    def __init__(self):
        self.description = 'Unknown Beverage'
        
    def getDescription(self):
        return self.description
    
    def cost(self):
        pass

      
class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
        
    def cost(self):
        return 1.99

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"
        
    def cost(self):
        return 1.05

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "HouseBlend"
        
    def cost(self):
        return 0.89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "DarkRoast"
        
    def cost(self):
        return 0.99
    
    
class CondimentDecorator(Beverage):
    def getDescription(self):
        pass

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + " Mocha"
    
    def cost(self):
        return 0.2 + self.beverage.cost()

class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + " Milk"
    
    def cost(self):
        return 0.1 + self.beverage.cost()

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + " Soy"
    
    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + " Whip"
    
    def cost(self):
        return 0.1 + self.beverage.cost()
    
    
beverage = Espresso()
print(beverage.getDescription(), beverage.cost())

beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print(beverage2.getDescription(), beverage2.cost())

beverage3 = HouseBlend()
beverage3 = Soy(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print(beverage3.getDescription(), beverage3.cost())
