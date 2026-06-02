import mediapipe as mp
from webcam import webcam_frames
from hand_tracker import HandTracker
import cv2

print("Welcome to AirDraw")
tracker = HandTracker()

for frame in webcam_frames():
    results = tracker.detect_hands(frame)
    print(len(results.hand_landmarks))
    cv2.imshow("Webcam AirDraw", frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()