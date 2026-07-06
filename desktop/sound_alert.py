import os

def play_alert_sound():

    sound_path = os.path.join(
        os.path.dirname(__file__),
        "../sounds/alert.wav"
    )

    #play sound using linux aplay
    os.system(f"aplay {sound_path}")


if __name__ == "__main__":
    print("Playing Alert Sound...")
    play_alert_sound()
