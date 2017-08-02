class MenuItem(object):

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

class Menu(object):
    def createIterator(self):
        pass

class PancakeHouseMenu(Menu):

    def __init__(self):
        self.menuItems = []
        self.addItem("K&B's Pancake Breafast", "Pancakes with scrambled eggs, and toast", True, 2.99)
        self.addItem("Regular Pancake Breafast", "Pancakes with fried eggs, and sausage", False, 2.99)
        self.addItem("blueberry Pancakes", "Pancakes made with fresh blueberry", True, 3.49)
        self.addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)

    def getMenuItems(self):
        return self.menuItems

    def createIterator(self):
        return PancakeHouseMenuIterator(self.menuItems)

class DinerMenu(Menu):

    def __init__(self):
        self.menuItems = []
        self.addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog", "A hot dog, with saurkraut, relish, onions, stoped with cheese", False, 3.05)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)

    def getMenuItems(self):
        return self.menuItems

    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

class CafeMenu(Menu):
    def __init__(self):
        self.menuItems = []
        self.addItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99)
        self.addItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69)
        self.addItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)

    def createIterator(self):
        return CafeMenuIterator(self.menuItems)

def TestPrintMenu():
    print("\n"+"*"*50 + "TestPrintMenu\n")
    pancakeHouseMenu = PancakeHouseMenu()
    breakfastItems = pancakeHouseMenu.getMenuItems()

    dinerMenu = DinerMenu()
    lunchItems = dinerMenu.getMenuItems()

    for item in breakfastItems:
        print("%s %s \n%s" % (item.getName(), item.getPrice(), item.getDescription()))

    for item in lunchItems:
        print("%s %s \n%s" % (item.getName(), item.getPrice(), item.getDescription()))


TestPrintMenu()

class Iterator(object):
    def hasNext(self):
        pass

    def next(self):
        pass

class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem

    def hasNext(self):
        if self.position >= len(self.items):
            return False
        else:
            return True

class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem

    def hasNext(self):
        if self.position >= len(self.items):
            return False
        else:
            return True

class CafeMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem

    def hasNext(self):
        if self.position >= len(self.items):
            return False
        else:
            return True

class Waitress(object):
    def __init__(self, pancakeHouseMenu, dinerMenu, cafeMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu

    def printMenu(self):
        pancakeIterator = self.pancakeHouseMenu.createIterator()
        dinerIterator = self.dinerMenu.createIterator()
        cafeIterator = self.cafeMenu.createIterator()
        print("MENU\n----\nBREAKFAST")
        self.__printMenu(pancakeIterator)
        print("\nLUNCH")
        self.__printMenu(dinerIterator)
        print("\nDINNER")
        self.__printMenu(cafeIterator)

    def __printMenu(self, iterator):
        while iterator.hasNext():
            menuItem = iterator.next()
            print("%s, %s-- %s" % (menuItem.getName(), menuItem.getPrice(), menuItem.getDescription()))

def TestIterator():
    print("\n"+"*"*50 + "TestIterator\n")
    pancakeMenu = PancakeHouseMenu()
    dinerMenu = DinerMenu()
    cafeMenu = CafeMenu()
    waitress = Waitress(pancakeMenu, dinerMenu, cafeMenu)
    waitress.printMenu()

TestIterator()

class CombinationWaitress(object):
    def __init__(self, menus):
        self.menus = menus

    def printMenu(self):
        for menu in self.menus:
            self.__printMenu(menu.createIterator())

    def __printMenu(self, iterator):
        while iterator.hasNext():
            menuItem = iterator.next()
            print("%s, %s-- %s" % (menuItem.getName(), menuItem.getPrice(), menuItem.getDescription()))

def TestCombinationIterator():
    print("\n"+"*"*50 + "TestCombinationIterator\n")
    pancakeMenu = PancakeHouseMenu()
    dinerMenu = DinerMenu()
    cafeMenu = CafeMenu()
    menus = [pancakeMenu, dinerMenu, cafeMenu]
    waitress = CombinationWaitress(menus)
    waitress.printMenu()

TestCombinationIterator()
