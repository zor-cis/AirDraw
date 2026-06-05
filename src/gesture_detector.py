import math


class GestureDetector:

    def is_pinching(self, landmarks):
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]

        distance = math.sqrt(
            (index_tip.x - thumb_tip.x) ** 2 +
            (index_tip.y - thumb_tip.y) ** 2 
        )
        return distance < 0.05