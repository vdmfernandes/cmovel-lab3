#!/bin/bash

sudo apt-get update
sudo apt-get install -y arduino arduino-core 
sudo apt-get install -y git-all

cd /usr/share/arduino/libraries/
sudo git clone https://github.com/markruys/arduino-DHT.git

mv arduino-DHT/ DHT
