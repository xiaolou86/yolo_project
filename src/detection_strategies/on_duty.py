from .detection_strategy import DetectionStrategy
from ultralytics import YOLO

"""
send alert if satisfying any of the following conditions:
    1) when person detected, the person keeps no move for 1 minute;
    2) when no persion detected for 5 minutes;
"""
class OnDutyDetectionStrategy(DetectionStrategy):
    def __init__(self, model):
        # need to use "yolov8n-pose.pt"
        self.model = YOLO(model)
        self.class_id = list(self.model.names.values()).index('person')  # Assuming 'person' is the class name for people

        self.no_move = False
        self.no_person = False
        self.last_time_no_move = 0
        self.last_time_no_person = 0
        self.persons = {}
    
    def detect(self, source):
        # Video setup
        videocapture = cv2.VideoCapture(source)
        frame_width, frame_height = int(videocapture.get(3)), int(videocapture.get(4))
        fps, fourcc = int(videocapture.get(5)), cv2.VideoWriter_fourcc(*"mp4v")

        # Output setup
        save_dir = increment_path(Path("outputs") / "exp", exist_ok)
        save_dir.mkdir(parents=True, exist_ok=True)
        video_writer = cv2.VideoWriter(str(save_dir / f"{Path(source).stem}.mp4"), fourcc, fps, (frame_width, frame_height))
    
        # Iterate over video frames
        while videocapture.isOpened():
            success, frame = videocapture.read()
            if not success:
                break
    
            # TODO: add logic
            results = self.model.track(frame)
            if len(results) <= 0:
                continue

            filter_boxes = results[0].boxes[results[0].boxes.cls == self.class_id]
            boxes = filter_boxes.xyxy.cpu()
            track_ids = filter_boxes.id.int().cpu().tolist()

            current_time = time.time()
            if len(boxes) == 0:
                if self.no_person == True:
                    if current_time - self.last_time_no_person > 60*5: # 300 seconds threshold
                        # TODO: alert
                        self.last_time_no_person = current_time
                else:
                    self.no_person = True
                    self.last_time_no_person = current_time
                continue

            self.no_person = False

            for box, track_id in zip(boxes, track_ids):
                # TODO: add logic for move
                if track_id not in self.persons:
                    self.persons[track_id] = box
                    self.no_move = False
                    continue
                else:
                    old_box = self.persons[track_id]

                    self.persons[track_id] = box



            video_writer.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

