import random

class Subject(object):
    def __init__(self):
        pass

    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass
    
    def notifyObserver(self):
        pass
    
class Observer(object):
    def __init__(self):
        pass
    
    def update(self, temp, humidity, pressure):
        pass
    
class DisplayElement(object):
    def __init__(self):
        pass
    
    def display(self):
        pass

class WeatherData(Subject):
    
    def __init__(self):
        super(WeatherData, self).__init__()
        self.temp = None
        self.humidity = None
        self.pressure = None
        self.observers = []
        
    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)
    
    def getTemperature(self):
        return self.temp
    
    def getHumidity(self):
        return self.humidity
    
    def getPressure(self):
        return self.pressure
    
    def measurementChanged(self):
        self.temp = random.randint(0, 100)
        self.humidity = random.randint(0, 100)
        self.pressure = random.randint(0, 100)
        
        self.notifyObserver()
    
class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, subject):
        super(CurrentConditionsDisplay, self).__init__()
        self.subject = subject

        subject.registerObserver(self)
    
    def update(self, temp, humidity, pressure):
        self.display(temp, humidity, pressure)
    
    def display(self, temp, humidity, pressure):
        name = self.__class__.__name__
        print("%s:(%02d-%02d-%02d)" % (name, temp, humidity, pressure))

class StatisticsPlay(object):
    pass

class forecastDisplay(object):
    pass

class ThirdPartyDisplay(object):
    pass

subject = WeatherData()
display = CurrentConditionsDisplay(subject)

for i in range(10):
    subject.measurementChanged()
