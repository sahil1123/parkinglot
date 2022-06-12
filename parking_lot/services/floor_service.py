from parking_lot.services.floor_service_interface import FloorServiceInterface
from parking_lot.models.floor import Floor
from parking_lot.services.slot_service import SlotService

class FloorService(FloorServiceInterface):
    floorDetails = {}
    def addFloor(self, parkingLotId, floorNumber, slots):
        floor = Floor()
        floor.setParkingLotId(parkingLotId)
        floor.setFloorNumber(floorNumber)

        slotsList = []
        for i in range(0,i):
            slot = SlotService()
            slotsList.append(slot)

        floor.setSlots(slots)

        self.__class__.floorDetails[f"{parkingLotId}_{floorNumber}"] = floor
        return floor