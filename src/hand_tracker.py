from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp
import cv2
from pathlib import Path

class HandTracker: 
    def __init__(self):
        model_path = (Path(__file__).parent/"assets"/"hand_landmarker.task")
        base_options = python.BaseOptions(model_asset_path= str(model_path))
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
        self.detector = vision.HandLandmarker.create_from_options(options)

    def detect_hands(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        return self.detector.detect(mp_image)