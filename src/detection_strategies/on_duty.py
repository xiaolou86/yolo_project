from .detection_strategy import DetectionStrategy

class OnDutyDetectionStrategy(DetectionStrategy):
    def __init__(self, model):
        self.model = model
    
    def detect(self, frame):
        results = self.model.predict(frame)
        detections = []
        for result in results:
            x1, y1, x2, y2, conf, cls = result
            detections.append((x1, y1, x2, y2, conf, cls))
        return detections

