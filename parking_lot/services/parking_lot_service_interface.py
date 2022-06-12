
import abc

class ParkingLotServiceInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def addParkingLot(self, id, numOfFloors, numOfSlots):
        pass