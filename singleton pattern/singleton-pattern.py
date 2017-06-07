#decorator method
def singleton(cls, *args, **kw):
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton 

@singleton
class ChocolateBoiler(object):
    
    def __init__(self):
        self.empty = True
        self.boiled = False
    
    def fill(self):
        if self.isEmpty():
            self.empty = False
            self.boiled = False
    
    def drain(self):
        if not self.isEmpty and self.isBoiled():
            self.empty = True
    
    def boil(self):
        if not self.isEmpty() and not self.isBoiled():
            self.boiled = True
    
    def isEmpty(self):
        return empty
    
    def isBoiled(self):
        return boided

#simple method
g_chocolate_boiler = None
def getInstance():
    if g_chocolate_boiler is None:
        g_chocolate_boiler = ChocolateBoiler()
    return g_chocolate_boiler

#other methods about __new__, __metaclass__ ...
