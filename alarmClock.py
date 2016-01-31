import schedule
import time
import subprocess


def job():
    print("Python should execute bash script")
    subprocess.call("./alarmClockBashScript.sh")


schedule.every().day.at("6:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
