import smtplib
from email.mime.text import MIMEText
from .alert_observer import AlertObserver

class EmailAlert(AlertObserver):
    def __init__(self, email, password, smtp_server, smtp_port):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def send_alert(self, detection_info):
        msg = MIMEText(f'Alert: {detection_info}')
        msg['Subject'] = 'YOLOv8 Detection Alert'
        msg['From'] = self.email
        msg['To'] = 'admin@example.com'
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.login(self.email, self.password)
            server.send_message(msg)

