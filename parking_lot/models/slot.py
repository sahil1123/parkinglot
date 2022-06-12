

class Slot(object):
    def __init__(self):
        self.slotNumber = None
        self.floorNumber = None
        self.type = None
        self.vehicle = None
        self.isBooked = False

    def getSlotNumber(self):
        return self.slotNumber

    def setSlotNumber(self, slotNumber):
        self.slotNumber = slotNumber

    def getFloorNumber(self):
        return self.floorNumber

    def setFloorNumber(self, floorNumber):
        self.floorNumber = floorNumber
    
    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def getIsBooked(self):
        return self.isBooked

    def setIsBooked(self, isBooked):
        self.isBooked = isBooked