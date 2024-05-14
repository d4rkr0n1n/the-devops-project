#!/bin/bash

rm -rf the-devops-project

git clone https://github.com/d4rkr0n1n/the-devops-project.git

cd /var/www/html

sudo cp -rf /home/vagrant/the-devops-project/web/* .

sudo python3 create_or_update_webpage.py &