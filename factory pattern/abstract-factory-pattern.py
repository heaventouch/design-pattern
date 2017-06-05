class ThinCrustDough(object):
    pass

class MarinaraSause(object):
    pass

class ReggianoCheese(object):
    pass

class Garlic(object):
    pass

class Onion(object):
    pass

class Mushroom(object):
    pass

class RedPepper(object):
    pass

class SlicedPepperoni(object):
    pass

class FreshClam(object):
    pass

class PlimTomotoSause(object):
    pass

class MozzarellaCheese(object):
    pass

class PlimTomotoSause(object):
    pass

class BlackOlives(object):
    pass

class Splinach(object):
    pass

class Eggplant(object):
    pass

class FrozenClam(object):
    pass


class PizzaIngredientFactory(object):
    def __init__(self):
        pass
    
    def createDough(self):
        pass
    
    def createSauce(self):
        pass
    
    def createCheese(self):
        pass
    
    def createVeggies(self):
        pass
    
    def createPepperoni(self):
        pass
    
    def createClam(self):
        pass
    
class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSause()
 
    def createCheese(self):
        return ReggianoCheese()
    
    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClam()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    
    def createDough(self):
        return ThickCrustDough()
    
    def createSauce(self):
        return PlimTomotoSause()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createVeggies(self):
        veggies = [BlackOlives(), Splinach(), Eggplant()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FrozenClam()

class Pizza(object):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None
    
    def prepare(self):
        pass
    
    def bake(self):
        print("Bake 25 minutes at 350")
        
    def cut(self):
        print("Cutting the pizza into diagonal sloces")
        
    def box(self):
        print("Place pizza in offlicial PizzaStore box")
    
    def setName(self, name):
        self.name = name
    
    def toString(self):
        pass

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        super(CheesePizza, self).__init__()
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Preparing %s" % self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
    
class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        super(CheesePizza, self).__init__()
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Preparing %s" % self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()

class VeggiePizza(Pizza):
    pass

class PepperoniPizza(Pizza):
    pass
        
class PizzaStore(object):
    def __init__(self):
        pass
    
    def orderPizza(self, pizza_type):

        pizza = self.createPizza(pizza_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    def createPizza(self, pizza_type):
        pass

class NYPizzaStore(PizzaStore):
        
    def createPizza(self, pizza_type):
        pizza = None
        ingredientFactory = NYPizzaIngredientFactory()
        
        if pizza_type == "cheese":
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("NY Style Cheese Pizza")
        
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName("NY Style Veggie Pizza")
        
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredientFactory)
            pizza.setName("NY Style Clam Pizza")
        
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("NY Style Pepperoni Pizza")
        
        return pizza

nyPizzaStore = NYPizzaStore()
nyPizzaStore.orderPizza("cheese")
