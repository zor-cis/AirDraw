import numpy as np
import cv2

class Canvas:

    def __init__(self):
        self.canvas = None
        self.previous_point = None
    
    def initialize_canvas(self, frame):
       if self.canvas is None:
            self.canvas = np.zeros_like(frame)
    
    def draw(self, current_point):
        if self.previous_point is not None:
            cv2.line(
                self.canvas,
                self.previous_point,
                current_point,
                (255, 255, 255),
                6
            )
        self.previous_point = current_point
    
    def stop_drawing(self):
        self.previous_point = None
    
    def clear(self):
        self.canvas.fill(0)

    def get_canvas(self):
        return self.canvas