import os
import time


def shutdown(timer):
    minutes = timer * 60

    time.sleep(minutes)

    os.system("shutdown -s")


shutdown(1)
