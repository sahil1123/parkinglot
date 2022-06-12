
from parking_lot.services.vehicle_service_interface import VehicleServiceInterface
from parking_lot.models.vehicle import Vehicle

class VehicleService(VehicleServiceInterface):
    vehicleDetails = {}
    def addVehicle(self, registratioNumber, color, type):
        vehicle = Vehicle()
        vehicle.setRegistrationNumber(registratioNumber)
        vehicle.setColor(color)
        vehicle.setType(type)

        self.__class__.vehicleDetails[registratioNumber] = vehicle
        return vehicle