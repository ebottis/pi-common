#!/bin/sh
#launchproject.sh

#called on boot
#sends IP to mobile phone in deets file
#runs project py

cd /
cd /home/pi/Projects
sleep 5s
python3 send_ip.py
python3 hawkeye.py

cd /
