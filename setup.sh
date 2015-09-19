#!/bin/bash

clear
echo
echo

echo -e "\e[1;33mInstalling Filezilla.\e[0m"
if [ -n "$(command -v apt-get)" ]; then
    apt-get -y install python3

elif [ -n "$(command -v pacman)" ]; then
    pacman -S python
else
    echo "apt-get and pacman aren't the current package managers?"
    exit 
