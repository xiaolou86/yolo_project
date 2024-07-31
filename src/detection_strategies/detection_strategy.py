from abc import ABC, abstractmethod

class DetectionStrategy(ABC):
	@abstractmethod
	def detect(self, source):
		pass

