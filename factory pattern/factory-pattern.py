class Pizza(object):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.topping = []
    
    def prepare(self):
        print("Preparing %s" % self.name)
        print("Tossing dpugh...")
        print("Adding sauce...")
        print("Adding toppings:")
        for i in self.topping:
            print(i)
    
    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")
    
    def getName(self):
        return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        
        self.topping.append("Grated Reggiano Cheese")

class NYStyleVeggiePizza(Pizza):
    pass

class NYStyleClamPizza(Pizza):
    pass

class NYStylePepperoniPizza(Pizza):
    pass

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        
        self.topping.append("Shredded Mozzarella Cheese")
    
    def cut(self):
        print("Cutting the pizza into square slices")

class ChicagoStyleVeggiePizza(Pizza):
    pass

class ChicagoStyleClamPizza(Pizza):
    pass

class ChicagoStylePepperoniPizza(Pizza):
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
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        
        else:
            return None

class ChicagoPizzaStore(PizzaStore):
    
    def createPizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        
        else:
            return None

nyStore = NYPizzaStore()
chicagoStore = ChicagoPizzaStore()

pizza = nyStore.orderPizza("cheese")
print("Ethan ordered a %s\n" % pizza.getName())

pizza = chicagoStore.orderPizza("cheese")
print("Joel ordered a %s\n" % pizza.getName())
