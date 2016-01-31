import schedule
import time
import subprocess


def job():
    print("Python should execute bash script")
    subprocess.call("./alarmClockBashScript.sh")


schedule.every().day.at("11:20").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
