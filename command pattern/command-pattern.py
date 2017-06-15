class Light(object):
    def __init__(self):
        pass
    
    def on(self):
        print("light on")
    
    def off(self):
        print("light off")
    
    def dim(self):
        print("light dim")

class Command(object):
    def __init__(self):
        pass
    
    def execute(self):
        pass

    def undo(self):
        pass
    
class LightOnCommand(Command):
    def __init__(self, light):
        super(LightOnCommand, self).__init__()
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        super(LightOffCommand, self).__init__()
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()
        
    
class SimpleRemoteControl(object):
    def __init__(self):
        self.slot = None
    
    def setCommand(self, command):
        self.slot = command
    
    def buttonWasPressed(self):
        self.slot.execute()
    
    def undoButtonWasPressed(self):
        self.slot.undo()

def remoteControlTest():
    remote = SimpleRemoteControl()
    light = Light()
    command = LightOnCommand(light)
    
    remote.setCommand(command)
    remote.buttonWasPressed()
    remote.undoButtonWasPressed()
    
#基本命令模式
remoteControlTest()

class NoCommand(Command):
    def __init__(self):
        super(NoCommand, self).__init__()
    
    def execute(self):
        print("no command")

class RemoteControlWithUndo(object):
    def __init__(self):
        self.onCommand = []
        self.offCommand = []
        
        noCommand = NoCommand()
        for i in range(7):
            self.onCommand.append(noCommand)
            self.offCommand.append(noCommand)
            
        self.undoCommand = noCommand
        
    def setCommand(self, slot, onCommand, offCommand):
        self.onCommand[slot] = onCommand
        self.offCommand[slot] = offCommand
    
    def onButtenWasPushed(self, slot):
        self.onCommand[slot].execute()
        self.undoCommand = self.onCommand[slot]
    
    def offButtenWasPushed(self, slot):
        self.offCommand[slot].execute()
        self.undoCommand = self.offCommand[slot]
    
    def undoButtenWasPushed(self):
        self.undoCommand.undo()

class CeilingFan(object):
    
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    
    def __init__(self):
        self.speed = None
    
    def high(self):
        self.speed = CeilingFan.HIGH
        print("ceiling fan set high")
    
    def medium(self):
        self.speed = CeilingFan.MEDIUM
        print("ceiling fan set medium")
    
    def low(self):
        self.speed = CeilingFan.LOW
        print("ceiling fan set low")
    
    def off(self):
        self.speed = CeilingFan.OFF
        print("ceiling fan set off")
    
    def getSpeed(self):
        return self.speed
    
class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        super(CeilingFanHighCommand, self).__init__()
        self.ceilingFan = ceilingFan
        self.prevSpeed = None
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()
    
    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        super(CeilingFanOffCommand, self).__init__()
        self.ceilingFan = ceilingFan
        self.prevSpeed = None
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()
    
    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()

def RemoteLoaderTest():
    remoteControl = RemoteControlWithUndo()
    ceilingFan = CeilingFan()
    
    ceilingFanHighCommand = CeilingFanHighCommand(ceilingFan)
    ceilingFanOffCommand = CeilingFanOffCommand(ceilingFan)
    remoteControl.setCommand(0, ceilingFanHighCommand,ceilingFanOffCommand)
    
    remoteControl.onButtenWasPushed(0)
    remoteControl.offButtenWasPushed(0)
    remoteControl.undoButtenWasPushed()

#多状态撤销
RemoteLoaderTest()
    

class TV(object):
    def __init__(self):
        pass
    
    def on(self):
        print("TV on")
    
    def off(self):
        print("TV off")
    
    def setInputChannel(self):
        print("TV set input channel")
    
    def setVolume(self):
        print("TV set volume")

class TVOnCommand(Command):
    def __init__(self, tv):
        super(TVOnCommand, self).__init__()
        self.tv = tv
    
    def execute(self):
        self.tv.on()

class TVOffCommand(Command):
    def __init__(self, tv):
        super(TVOffCommand, self).__init__()
        self.tv = tv
    
    def execute(self):
        self.tv.off()

class Stereo(object):
    def __init__(self):
        pass
    
    def on(self):
        print("stereo on")
    
    def off(self):
        print("stereo off")
    
    def setCd(self):
        print("stereo set CD")
    
    def setDvd(self):
        print("stereo set DVD")
    
    def setRadio(self):
        print("stereo set radio")
    
    def setVolume(self):
        print("stereo set volume")

class StereoOnCommand(Command):
    def __init__(self, stereo):
        super(StereoOnCommand, self).__init__()
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        super(StereoOffCommand, self).__init__()
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()

class Hottub(object):
    def __init__(self):
        pass
    
    def on(self):
        print("hot tub on")
    
    def off(self):
        print("hot tub off")
    
    def circulate(self):
        print("hot tub circulate")
        
    def jetsOn(self):
        print("hot tub jets on")
    
    def jetsOff(self):
        print("hot tub jets off")
    
    def setTemperature(self):
        print("hot tub set temperature")

class HottubOnCommand(Command):
    def __init__(self, bottub):
        super(HottubOnCommand, self).__init__()
        self.bottub = bottub
    
    def execute(self):
        self.bottub.on()

class HottubOffCommand(Command):
    def __init__(self, bottub):
        super(HottubOffCommand, self).__init__()
        self.bottub = bottub
    
    def execute(self):
        self.bottub.off()

        
class MacroCommand(Command):
    def __init__(self, commands):
        super(MacroCommand, self).__init__()
        self.commands = commands
    
    def execute(self):
        for command in self.commands:
            command.execute()
    
    def undo(self):
        for command in self.commands:
            command.undo()

def MacroTest():
    light = Light()
    tv = TV()
    stereo = Stereo()
    hottub = Hottub()
    
    lightOnCommand = LightOnCommand(light)
    tvOnCommand = TVOnCommand(tv)
    stereoOnCommand = StereoOnCommand(stereo)
    hottubOnCommand = HottubOnCommand(hottub)
    
    lightOffCommand = LightOffCommand(light)
    tvOffCommand = TVOnCommand(tv)
    stereoOffCommand = StereoOffCommand(stereo)
    hottubOffCommand = HottubOffCommand(hottub)
    
    partyOn = [lightOnCommand, tvOnCommand, stereoOnCommand, hottubOnCommand]
    partyOff = [lightOffCommand, tvOffCommand, stereoOffCommand, hottubOffCommand]
    
    partyOnCommand = MacroCommand(partyOn)
    partyOffCommand = MacroCommand(partyOff)
    
    remoteCommand = RemoteControlWithUndo()
    remoteCommand.setCommand(0, partyOnCommand, partyOffCommand)
    
    remoteCommand.onButtenWasPushed(0)
    remoteCommand.offButtenWasPushed(0)

#宏命令
MacroTest()
