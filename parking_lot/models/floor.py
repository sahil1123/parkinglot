
class Floor(object):
    def __int__(self):
        self.slots = []
        self.floorNumber = None
        self.parkingLotId = None

    def getSlots(self):
        return self.slots
    
    def setSlots(self, slots):
        self.slots = slots

    def getFloorNumber(self):
        return self.floorNumber

    def setFloorNumber(self, floorNumber):
        self.floorNumber = floorNumber

    def getParkingLotId(self):
        return self.parkingLotId

    def setParkingLotId(self, parkingLotId):
        self.parkingLotId = parkingLotId
