import logging
from .alert_observer import AlertObserver

class LoggingAlert(AlertObserver):
    def __init__(self, log_file):
        self.logger = logging.getLogger('DetectionLogger')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)
    
    def send_alert(self, detection_info):
        self.logger.info(f'Alert: {detection_info}')

