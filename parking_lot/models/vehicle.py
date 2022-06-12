class Vehicle(object):
    def __init__(self):
        self.type = None
        self.registrationNumber = None
        self.color = None
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type

    def getRegistrationNumber(self):
        return self.registrationNumber

    def setRegistrationNumber(self, registrationNumber):
        self.registrationNumber = registrationNumber

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color