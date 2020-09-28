#!/bin/bash
clear
echo -e "\e[4;34m This script  Was Created By Khan \e[0m"

echo "This is version 0.1 beta"
toilet -f mono12 -F border KHAN

figlet ResultMaker | lolcat
python3 result.py result.txt
clear
cat result.txt  | lolcat

