import sys
from datetime import datetime
from time import sleep


while True:
    sys.stdout.write("Date:"+datetime.date(datetime.now()).strftime("%d/%m/%Y")+", Time:"+datetime.time(datetime.now())
                     .strftime("%H:%M:%S")+"\n")
    sleep(1)
