import mediapipe as mp
from canvas import Canvas
from gesture_detector import GestureDetector
from renderer import Renderer
from webcam import webcam_frames
from hand_tracker import HandTracker
import cv2

print("Welcome to AirDraw")

tracker = HandTracker()
detector = GestureDetector()
canvas = Canvas()
renderer = Renderer()


for frame in webcam_frames():

    canvas.initialize_canvas(frame)

    result = tracker.detect_hands(frame)
    landmarks = tracker.get_landmarks(result)

    if landmarks:
        if detector.is_pinching(landmarks):
            point = tracker.get_index_position(landmarks, frame)
            canvas.draw(point)
        else:
            canvas.stop_drawing()

    output = renderer.render(frame, canvas.get_canvas())                 
    cv2.imshow("Webcam AirDraw", output)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()