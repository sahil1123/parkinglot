
import abc
class VehicleServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addVehicle(self,registratioNumber, color, type):
		pass