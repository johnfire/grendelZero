#!/bin/bash
#script to upgrade all computers
echo "!-! 		Updating  apt on 110"
sudo apt update
echo "!-!		Updating apt on 101"
ssh pi@192.168.0.101 sudo apt update
echo "!-!		Updating apt on 102"
ssh pi@192.168.0.102 sudo apt update
echo "!-!		Updating apt on 103"
ssh pi@192.168.0.103 sudo apt update
echo "!-!		Updating apt on 104"
ssh pi@192.168.0.104 sudo apt update
echo "!-!		Updating apt on 105"
ssh pi@192.168.0.105 sudo apt update
echo "!-!		Updating apti on 106"
ssh pi@192.168.0.106 sudo apt update
#echo "!-!		Updating apt on 107"
#ssh pi@192.168.0.107 sudo apt update
#sleep 2m
echo "!-!		Doing upgrade  on 101"
ssh pi@192.168.0.101 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 102"
ssh pi@192.168.0.102 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 103"
ssh pi@192.168.0.103 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 104"
ssh pi@192.168.0.104 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 105"
ssh pi@192.168.0.105 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 106"
ssh pi@192.168.0.106 sudo apt -y upgrade
echo "!-!		Doing upgrade  on 110"
sudo apt -y dist-upgrade

echo "!-! 		Now running autoremove on 101"
ssh pi@192.168.0.101 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 102"
ssh pi@192.168.0.102 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 103"
ssh pi@192.168.0.103 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 104"
ssh pi@192.168.0.104 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 105"
ssh pi@192.168.0.105 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 106"
ssh pi@192.168.0.106 sudo apt -y autoremove
echo "!-! 		Now running autoremove on 110"
sudo apt -y autoremove



