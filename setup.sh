#!/bin/bash

clear
echo
echo

echo -e "\e[1;33mInstalling Python.\e[0m"
if [ -n "$(command -v apt-get)" ]; then
    apt-get -y install python3

elif [ -n "$(command -v pacman)" ]; then
    pacman -S python
fi 
