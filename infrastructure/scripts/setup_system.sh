#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip apache2 -y

sudo pip install bitmath
sudo pip install psutil

sudo systemctl enable --now apache2