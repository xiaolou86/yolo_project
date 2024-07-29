from abc import ABC, abstractmethod

class AlertObserver(ABC):
    @abstractmethod
    def send_alert(self, detection_info):
        pass

