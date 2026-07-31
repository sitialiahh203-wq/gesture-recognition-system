import cv2


class TextAnimation:

    def __init__(self):
        self.scale = 1
        self.alpha = 0

    def draw_text(self, frame, text):

        if self.alpha < 255:
            self.alpha += 5

        overlay = frame.copy()

        font = cv2.FONT_HERSHEY_SIMPLEX

        size = cv2.getTextSize(
            text,
            font,
            2,
            4
        )[0]


        x = int((frame.shape[1] - size[0]) / 2)
        y = int(frame.shape[0] / 2)


        cv2.putText(
            overlay,
            text,
            (x,y),
            font,
            2,
            (0,255,255),
            4
        )


        cv2.addWeighted(
            overlay,
            self.alpha / 255,
            frame,
            1 - self.alpha / 255,
            0,
            frame
        )