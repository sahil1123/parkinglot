from parking_lot.services.parking_lot_service_interface import ParkingLotServiceInterface
from parking_lot.models.parking_lot import ParkingLot
from parking_lot.services.floor_service import FloorService

class ParkingLotService(ParkingLotServiceInterface):
    parkingLotDetails = {}
    def addParkingLot(self, id, numOfFloors, numOfSlots):
        parkingLot = ParkingLot()
        parkingLot.setId(id)

        floorsList = []
        for floorNum in range(0, numOfFloors):
            floor = FloorService()
            floor.addFloor(id, floorNum, numOfSlots)
            
            floorsList.append(floor)
            # in floor - add slots
            # append slots to floor list in floor Service
        
        parkingLot.setFloors(floorsList)

        self.__class__.parkingLotDetails[id] = parkingLot
        return parkingLot