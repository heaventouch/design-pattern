
class Duck(object):
    def quack(self):
        pass
    
    def fly(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        print("Quck")
        
    def fly(self):
        print("I am flying")

class Turkey(object):
    def gobble(self):
        pass
    
    def fly(self):
        pass

class WileTurkey(Turkey):
    def gobble(self):
        print("Gobble")
    
    def fly(self):
        print("I am flying a short distance")

class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
    
    def quack(self):
        self.turkey.gobble()
    
    def fly(self):
        for i in range(5):
            self.turkey.fly()

def TestTurkeyAdapter():
    turkey = WileTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)
    turkeyAdapter.quack()
    turkeyAdapter.fly()
