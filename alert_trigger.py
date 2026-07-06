def trigger_alert(message):

    print("\n ALERT ")
    print("Message:", message)
    try:
        import os
        os.system("aplay sounds/alert.wav")
    except Exception as e:
        print(" Sound not supported on server ")

    try:
        import subprocess
        subprocess.Popen(["notify-send", message])
    except Exception as e:
        print(" Popup not supported on server") 
