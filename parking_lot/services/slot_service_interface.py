import abc

class SlotServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addSlot(self, slotNumber, floorNumber, type, vehicle, isBooked):
        pass