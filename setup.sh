#!/bin/bash
clear
echo -e "\033[91mPicolas\033[0m DDOS Tool,"
echo -e "Please Wait..."
apt-get -y update > /dev/null 2>&1
apt-get -y install python3 python3-pip > /dev/null 2>&1
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip3 install requests > /dev/null 2>&1
pip3 install pyfiglet > /dev/null 2>&1
clear
echo -e "\033[92m[*]\033[0m \033[91mPicolas\033[0m DDOS Tool was installed successfully."
echo -e "\n\nTo run it type 'python3 picolas_ddos_tool.py'\n"
