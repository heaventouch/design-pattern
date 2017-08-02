import exceptions

class MenuComponent(object):
    def add(self, menuComponent):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def remove(self, menuComponent):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def getChild(self, i):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def getName(self):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def getDescription(self):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def getPrice(self):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def isVegetarian(self):
        raise exceptions.NotImplementedError, "base class method not implemented"

    def _print(self):
        raise exceptions.NotImplementedError, "base class method not implemented"

class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def isVegetarian(self):
        return self.vegetarian

    def _print(self):
        print(" " + self.getName() + ("(V)" if self.isVegetarian() else "") + str(self.getPrice()))
        print("    --" + self.getDescription())

class Menu(MenuComponent):
    def __init__(self, name, description):
        self.menuComponents = []
        self.name = name
        self.description = description

    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self.menuComponents[i]

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def _print(self):
        print("\n" + self.getName() + ", " + self.getDescription() + "\n" + "*"*20)
        for _menu in self.menuComponents:
            _menu._print()

class Waitress(object):
    def __init__(self, allMenus):
        self.allMenus = allMenus

    def printMenus(self):
        self.allMenus._print()

def TestMenuDrive():
    pancakeHouseMenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    dinnerMenu = Menu("DINNER MENU", "Lunch")
    cafeMenu = Menu("CAFE MENU", "Dinner")
    dessertMenu = Menu("DESSERT MENU", "Dessert of course!")

    allMenus = Menu("ALL MENUS", "All menus combined")

    allMenus.add(pancakeHouseMenu)
    allMenus.add(dinnerMenu)
    allMenus.add(cafeMenu)

    dinnerMenu.add(MenuItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89))

    dinnerMenu.add(dessertMenu)

    dessertMenu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla ice cream", True, 1.59))

    waitress = Waitress(allMenus)
    waitress.printMenus()

TestMenuDrive()
