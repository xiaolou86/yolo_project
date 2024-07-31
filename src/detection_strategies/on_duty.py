from .detection_strategy import DetectionStrategy
from ultralytics import YOLO

class OnDutyDetectionStrategy(DetectionStrategy):
    def __init__(self, model):
        self.model = YOLO(model)
    
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

            video_writer.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

