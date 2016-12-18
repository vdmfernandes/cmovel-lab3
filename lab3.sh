#!/bin/bash

sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential 
sudo apt-get install -y arduino arduino-core 
sudo apt-get install -y git-all

sudo pip install pyserial

cd /usr/share/arduino/libraries/
sudo git clone https://github.com/markruys/arduino-DHT.git

mv arduino-DHT/ DHT
