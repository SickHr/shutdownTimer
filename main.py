import os
import time

def shutdown(timer):
    minutes = timer

    for remaining_time in range(minutes, 0, -1):
        print(f"Remaining time till shutdown: {remaining_time} minutes")
        time.sleep(60)  # hier wird 60 Sekunden gewartet, da wir in Minuten zählen

    print("Shutting down...")
    os.system("shutdown -s")

shutdown(60)  # Hier kannst du die gewünschte Zeit in Minuten ändern
