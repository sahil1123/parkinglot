

import abc

class FloorServiceInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def addFloor(self, parkingLotId, floorNumber, slots):
        pass