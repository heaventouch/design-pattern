import random

class GumballMachine(object):
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3
    def __init__(self, count):
        self.state = GumballMachine.SOLD_OUT
        self.count = count
        if count > 0:
            self.state = GumballMachine.NO_QUARTER

    def insertQuarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("You cna't insert another quarter")
        elif self.state == GumballMachine.NO_QUARTER:
            self.state = GumballMachine.HAS_QUARTER
            print("You insert a quarter")
        elif self.state == GumballMachine.SOLD_OUT:
            print("You cannt insert a quarter, the machine is sold out")
        elif self.state == GumballMachine.SOLD:
            print("Please wait, we are already giving you a gumball")


    def ejectQuarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("Quarter return")
            self.state = GumballMachine.NO_QUARTER
        elif self.state == GumballMachine.NO_QUARTER:
            print("you turned but there is no quarter")
        elif self.state == GumballMachine.SOLD:
            print("you turned, but there are no gumball")
        elif self.state == GumballMachine.SOLD_OUT:
            print("you cannt eject, you have not inserted a quarter yet")

    def turnCrank(self):
        if self.state == GumballMachine.SOLD:
            print("Turning twice doesnot get you another gumball")
        elif self.state == GumballMachine.NO_QUARTER:
            print("you turned but there is no quarter")
        elif self.state == GumballMachine.SOLD_OUT:
            print("you turned, but there are no gumball")
        elif self.state == GumballMachine.HAS_QUARTER:
            print("you turned...")
            self.state = GumballMachine.SOLD
            self.dispense()

    def dispense(self):
        if self.state == GumballMachine.SOLD:
            print("A gumball come rolling out the slot")
            self.count -= 1
            if self.count == 0:
                print("Oops, out of gumball")
                self.state = GumballMachine.SOLD_OUT
            else:
                self.state = GumballMachine.NO_QUARTER

        elif self.state == GumballMachine.NO_QUARTER:
            print("you need to pay first")

        elif self.state == GumballMachine.SOLD_OUT:
            print("No gumball dispensed")

        elif self.state == GumballMachine.HAS_QUARTER:
            print("No gumball dispensed")

    def __repr__(self):
        return ("GumballMachine state:%d count:%d" % (self.state, self.count))

def GumballMachineTest():
    gumballMachine = GumballMachine(5)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

#GumballMachineTest()


class State(object):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("you inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("you have not inserted a quarter")

    def turnCrank(self):
        print("you turned, but there is no quarter")

    def dispense(self):
        print("you need to pay first")

class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("you can not insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("you turned...")
        winner = random.randint(0, 10)
        if winner == 0 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("no gumball dispensed")

class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("please wait, we are already giving you a gumball")

    def ejectQuarter(self):
        print("sorry, you already turned the crank")

    def turnCrank(self):
        print("turning twice does not get another gumball")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumball")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("you can not insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("you can not eject, you hace not inserted a quarter yet")

    def turnCrank(self):
        print("you turned, but there is no gumball")

    def dispense(self):
        print("no gumball dispensed")

class WinnerState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Err...")

    def ejectQuarter(self):
        print("Err...")

    def turnCrank(self):
        print("Err...")

    def dispense(self):
        print("you are a winner! you get two gumballs for your quarter")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            print("Oops, out of gumball")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class StateGumballMachine(object):
    def __init__(self, count):
        self.soldState = SoldState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarteState = HasQuarterState(self)
        self.soldOutState = SoldOutState(self)
        self.winnerState = WinnerState(self)

        self.state = self.soldOutState
        self.count = count
        if count > 0:
            self.state = self.noQuarterState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
        self.state = state

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1

    def getCount(self):
        return self.count

    def getSoldState(self):
        return self.soldState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarteState

    def getSoldOutState(self):
        return self.soldOutState

    def getWinnerState(self):
        return self.winnerState

    def __repr__(self):
        return ("StateGumballMachine state:%s count:%d" % (self.state, self.count))


def StateGumballMachineTest():
    gumballMachine = StateGumballMachine(5)

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

#StateGumballMachineTest()

def WinnerGumballMachineTest():
    gumballMachine = StateGumballMachine(5)

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

WinnerGumballMachineTest()
