#!/bin/bash
clear
echo -e "\e[4;31m KHAN Productions !!! \e[0m"
echo -e "\e[1;34m Presents \e[0m"
echo -e "\e[1;32m ResultMaker \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.khan ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet lolcat python curl -y
apt install python3-pip
pip install -r requirements.txt
echo This Script Was Made By KHAN >update.khan
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet ResultMaker | lolcat
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border KHAN
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
echo " "
echo "Press 1 To  Start ResultMaker "
echo "Press 2 To  Update (Works On Linux And Linux Emulators) "
echo "Press 3 To  View Features "
echo "Press 4 To  Exit "
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python3 result.py result.txt
clear
cat result.txt | lolcat
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
apt install git -y
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/Mubsshir/result.git
if [[ -s result/run.sh ]];then
cd result
cp -r -f * .. > temp
cd ..
rm -rf  result >> temp
rm update.khan >> temp
rm temp
chmod +x run.sh
fi
echo -e "\e[1;32m ResultMaker Restart Now..."
echo -e "\e[1;32m All The Required Packages Will Be Installed..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
./run.sh
exit
elif [ $ch -eq 3 ];then
clear
echo -e "\e[1;33m"
figlet Khan
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border KHAN
echo  " "
echo -e "\e[1;32m                   Features\e[1;34m"
echo "  [+] Very Basic ResultMaker created when I was learning python "
echo "Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;31m"
figlet ResultMaker | lolcat
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border KHAN
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done

