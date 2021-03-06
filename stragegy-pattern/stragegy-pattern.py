class Duck(object):
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None
        
    
    def swim(self):
        print("swim")
    
    def display(self):
        pass
    
    def performQuack(self):
        self.quackBehavior.quack()
    
    def performFly(self):
        self.flyBehavior.fly()
    
    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior
    
    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior


class FlyBehavior(object):
    def __init__(self):
        pass
    
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("FlyWithWings")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("FlyNoWay")


class QuackBehavior(object):
    def __init__(self):
        pass
    
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("MuteQuack")


class MallardDuck(Duck):
    
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()
        
    def display(self):
        pritn("MallardDuck")

mallard = MallardDuck()
mallard.performFly()
mallard.performQuack()
