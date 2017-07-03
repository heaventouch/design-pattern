class CaffeineBeverage(object):
    def __init__(self):
        pass
    
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()
    
    def boilWater(self):
        print("Boiling water")
    
    def brew(self):
        pass
    
    def pourInCup(self):
        print("Pouring in cup")
    
    def addCondiments(self):
        pass

class Tea(CaffeineBeverage):
    def __init__(self):
        super(Tea, self).__init__()
    
    def brew(self):
        print("Steeping the tea")
    
    def addCondiments(self):
        print("Adding Lemon")

class Coffee(CaffeineBeverage):
    def __init__(self):
        super(Coffee, self).__init__()
    
    def brew(self):
        print("Dripping Coffee through filter")
    
    def addCondiments(self):
        print("Adding Sugar and Milk")

def TestCaffeeineBeverage():
    tea = Tea()
    tea.prepareRecipe()
    
    coffee = Coffee()
    coffee.prepareRecipe()

TestCaffeeineBeverage()
    
    
class CaffeineBeverageWithHook(object):
    def __init__(self):
        pass
    
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()
    
    def boilWater(self):
        print("Boiling water")
    
    def brew(self):
        pass
    
    def pourInCup(self):
        print("Pouring in cup")
    
    def addCondiments(self):
        pass
    
    def customerWantsCondiments(self):
        return True

class CoffeeWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        super(CoffeeWithHook, self).__init__()
    
    def brew(self):
        print("Dripping Coffee through filter")
    
    def addCondiments(self):
        print("Adding Sugar and Milk")
    
    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer.lower()[0] == 'y':
            return True
        else:
            return False
    
    def getUserInput(self):
        answer = raw_input("Would you like milk and sugar with you caffee(y/n)? ")
        
        if not answer:
            return "no"
        
        return answer

def TestCoffineBeverageWithHook():
    coffee = CoffeeWithHook()
    coffee.prepareRecipe()

TestCoffineBeverageWithHook()
