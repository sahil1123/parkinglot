class ParkingLotController(object):
	def __init__(self, parkingLotService):
		self.parkingLotService = parkingLotService
	def addParkingLot(self, id, floors):
		return self.parkingLotService.addParkingLot(id,floors)