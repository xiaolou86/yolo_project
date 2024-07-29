from detection_strategies.on_duty import OnDutyDetectionStrategy
from alert_system.alert_system import AlertSystem
from alert_system.email_alert import EmailAlert
from alert_system.logging_alert import LoggingAlert
from camera import Camera

# Initialize detection strategies
custom_strategy = OnDutyDetectionStrategy('yolov8.pt')

# Initialize alert system
alert_system = AlertSystem()

# Initialize alert methods
email_alert = EmailAlert('your_email@example.com', 'your_password', 'smtp.example.com', 587)
logging_alert = LoggingAlert('detection.log')

# Add alert methods to the alert system
#alert_system.add_observer(email_alert)
alert_system.add_observer(logging_alert)

# Initialize cameras with different strategies
camera2 = Camera(custom_strategy)

# Example detection info
detection_info = 'Detected person with confidence 0.95'

# Notify all observers (send alerts)
alert_system.notify_observers(detection_info)

## Capture and process frames from camera1
#camera1.capture_and_process()

# Capture and process frames from camera2
camera2.capture_and_process("datas/bus.jpg")

