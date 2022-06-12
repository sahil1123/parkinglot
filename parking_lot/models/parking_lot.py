class ParkingLot(object):
    def __init__(self):
        self.id = None
        self.floors = []

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getFloors(self):
        return self.floors

    def setFloors(self, floors):
        self.floors = floors