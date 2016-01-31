import schedule
import time
import subprocess

audio_file = "GriegEdvard_PeerGynt_MorningMood.mp3"


def job():
    print("Python should execute script")
    subprocess.call("./alarmClockBashScript.sh")


schedule.every().day.at("9:43").do(job)
schedule.every().day.at("9:48").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
