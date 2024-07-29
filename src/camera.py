import cv2
from detection_strategies.detection_strategy import DetectionStrategy

class Camera:
    def __init__(self, strategy: DetectionStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: DetectionStrategy):
        self.strategy = strategy
    
    def process_frame(self, frame):
        return self.strategy.detect(frame)
    
    def capture_and_process(self, camera_source):
        cap = cv2.VideoCapture(0)  # Adjust as necessary for your camera index
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            detections = self.process_frame(frame)
            for x1, y1, x2, y2, conf, cls in detections:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{cls} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

