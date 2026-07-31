import cv2

from hand_detector import HandDetector
from gesture import detect_gesture
from ui import draw_hud, add_cinematic_background
from animation import TextAnimation
from sound import play_sound

import mediapipe as mp

detector = HandDetector()
animation = TextAnimation()


mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("EROR")
    exit ()

while True:

    success, frame = cap.read()
    print("succes", success)

    if not success:
        print("Gagal")
        break

    frame = cv2.flip(frame, 1)


    result = detector.detect(frame)

    display_frame = add_cinematic_background(frame)

    draw_hud(frame)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                display_frame,
                hand,
                mpHands.HAND_CONNECTIONS
            )

            gesture = detect_gesture(hand)
            play_sound(gesture)

            animation.draw_text(
                display_frame,
                gesture
            )
            

    cv2.imshow("Hand Tracker",display_frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()