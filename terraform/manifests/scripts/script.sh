#!/bin/bash

sudo yum update -y && sudo yum upgrade -y
sudo yum install -y python3

python3 -m ensurepip --default-pip
pip3 install --upgrade pip
pip3 install flask