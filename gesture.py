def detect_gesture(hand_landmarks):

    fingers = []

    tips = [4, 8, 12, 16, 20]


    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)


    # 4 fingers
    for tip in tips[1:]:

        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y:
            fingers.append(1)
        else:
            fingers.append(0)


    total = sum(fingers)


    # ==========================
    # GESTURE INTRO OSPEK
    # ==========================


    # ✌️ Dua jari
    if fingers == [0,1,1,0,0]:
        return "Siti Aliah"


    # ☝️ Satu jari
    elif fingers == [0,1,0,0,0]:
        return "SMKN 1 GEBANG"


    # ✋ Lima jari
    elif total == 5:
        return "Cirebon"


    # 👍 Jempol
    elif fingers == [1,0,0,0,0]:
        return "SIKC"


    else:
        return f"FINGER: {total}"