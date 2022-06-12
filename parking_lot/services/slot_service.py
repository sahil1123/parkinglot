from parking_lot.services.slot_service_interface import SlotServiceInterface
from parking_lot.models.slot import Slot


class SlotService(SlotServiceInterface):
    slotDetails = {}
    def addSlot(self, slotNumber, floorNumber, type, vehicle=None, isBooked=False):
        slot = Slot()
        slot.setSlotNumber(slotNumber)
        slot.setFloorNumber(floorNumber)
        slot.setType(type)
        slot.setVehicle(vehicle)    
        slot.setIsBooked(isBooked)

        self.__class__.slotDetails[f"{floorNumber}_{slotNumber}"] = slot
        return slot
        