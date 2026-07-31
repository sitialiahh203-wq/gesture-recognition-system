import pygame

pygame.mixer.init()

sounds = {
    "Siti Aliah": pygame.mixer.Sound("assets/sounds/siti aliah.mp3"),
    "SMKN 1 GEBANG": pygame.mixer.Sound("assets/sounds/smk negeri 1 gebang.mp3"),
    "Cirebon": pygame.mixer.Sound("assets/sounds/cirebon.mp3"),
    "SIKC": pygame.mixer.Sound("assets/sounds/sikc.mp3"),
}

last_gesture = None

def play_sound(gesture):
    global last_gesture

    if gesture != last_gesture:
        last_gesture = gesture

        if gesture in sounds:
            sounds[gesture].play()
def play_sound(gesture):
    global last_gesture

    print("Gesture terdeteksi:", gesture)

    if gesture != last_gesture:
        last_gesture = gesture

        if gesture in sounds:
            print("Memutar:", gesture)
            sounds[gesture].play()
        else:
            print("Gesture tidak ditemukan di dictionary!")