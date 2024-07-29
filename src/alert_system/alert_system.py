from .alert_observer import AlertObserver

class AlertSystem:
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer: AlertObserver):
        self._observers.append(observer)
    
    def remove_observer(self, observer: AlertObserver):
        self._observers.remove(observer)
    
    def notify_observers(self, detection_info):
        for observer in self._observers:
            observer.send_alert(detection_info)

