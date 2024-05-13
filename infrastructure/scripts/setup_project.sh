#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip apache2 -y

sudo pip install bitmath
sudo pip install psutil

git clone https://github.com/d4rkr0n1n/the-devops-project.git

sudo cp the-devops-project/web/index_tmp.html /var/www/html/
sudo cp the-devops-project/web/styles.css /var/www/html/
sudo cp the-devops-project/web/create_or_update_webpage.py /var/www/html/

sudo systemctl enable --now apache2
sudo python3 create_or_update_webpage.py 