import schedule
import time
import vlc
import os
import sys
from datetime import datetime
audioNewYear = vlc.MediaPlayer("happy_new_year.mp3")
audioParty = vlc.MediaPlayer("party_music.mp3")
countDownStartTime="23:59"
newYearTime="00:00"
countDownEndTime=newYearTime
closeTime="00:01"
os.system("clear")
def audioPartyPlay():
    audioParty.play()
def audioPartyStop():
    audioParty.stop()
def countDownStart():
    for remaining in range(59,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} Seconds Left Until The Birth Of Next Year And Next Decade . . . ".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
def happyNewYear():
    print(datetime.now())
    os.system('./happy_new_year_text.sh')
    print("\n This Is A Brand New Year \n")
def audioNewYearPlay():
    audioNewYear.play()
def countDownBye():
    for remaining in range(59, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} Seconds Run Time For This New Year And New Decade . . . ".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n HAVE A AWESOME YEAR AHEAD ^**^ :) \n")
def audioNewYearStop():
    audioNewYear.stop()
def aheadFunc():
    endNow=datetime.now()
    audioParty.stop()
    exit()
schedule.every().day.at(countDownStartTime).do(audioPartyPlay)
schedule.every().day.at(countDownStartTime).do(countDownStart)
schedule.every().day.at(newYearTime).do(happyNewYear)
schedule.every().day.at(newYearTime).do(audioPartyStop)
schedule.every().day.at(newYearTime).do(audioNewYearPlay)
schedule.every().day.at(countDownEndTime).do(countDownBye)
schedule.every().day.at(closeTime).do(audioNewYearStop)
schedule.every().day.at(closeTime).do(aheadFunc)
while True:
    schedule.run_pending()
    time.sleep(1)
