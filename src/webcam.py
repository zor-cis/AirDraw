import cv2

def webcam_frames(camera_index = 0):

    cap = cv2.VideoCapture(camera_index) 
    
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")
        
    while True:
        success, frame = cap.read() 
        if not success:
            break

        frame = cv2.flip(frame, 1)

        yield frame

    cap.release()
    