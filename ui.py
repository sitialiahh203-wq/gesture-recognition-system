import cv2
import numpy as np

from config import *


def add_cinematic_background(frame):

    h, w, _ = frame.shape


    # Buat gradient background
    gradient = np.zeros_like(frame)


    for y in range(h):

        intensity = int(40 + (y / h) * 80)

        gradient[y, :, :] = (
            intensity,
            intensity // 2,
            intensity
        )


    # Blend kamera dengan background

    result = cv2.addWeighted(
        frame,
        0.65,
        gradient,
        0.35,
        0
    )

    return result



def draw_hud(frame):

    cv2.rectangle(
        frame,
        (20,20),
        (1260,700),
        HUD_COLOR,
        2
    )


    cv2.putText(
        frame,
        "HAND TRACKER SYSTEM",
        (40,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        TEXT_COLOR,
        2
    )