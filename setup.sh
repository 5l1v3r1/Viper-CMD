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

echo -e "\e[1;33mInstalling Xlib for arm devices.\e[0m"
if [ -n "$(command -v apt-get)" ]; then
    apt-get -y install libx11-dev

elif [ -n "$(command -v pacman)" ]; then
     pacman -S libx11-dev
fi

echo -e "\e[1;33mInstalling Xlib for python 3.\e[0m"
if [ -n "$(command -v apt-get)" ]; then
	    apt-get -y install python3-xlib

    elif [ -n "$(command -v pacman)" ]; then
	         pacman -S python3-xlib
fi
