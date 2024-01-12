#!/bin/bash
# Script to monitor the Massa node and restart it if it is not running
# Add the following to the crontab (i.e. crontab -e)
# */5 * * * * ~/massa-monitor.sh

# set vars
# read -p "Enter massa-client password: " PASSWORD
# PASSWORD=$PASSWORD
SLEEP=900
# DIR=$(pwd)
HOME_DIR=$HOME/massa/massa-client
cd $HOME_DIR
WALLET_ADDRESS=$(./massa-client wallet_info -p "$PASSWORD" | grep 'Address' | awk '{print $2}')


echo '================================================='
echo -e "massa-client folder path: \e[1m\e[32m${HOME_DIR}\e[0m"
echo -e "Massa wallet address: \e[1m\e[32m$WALLET_ADDRESS\e[0m"
echo -e "Sleep time: \e[1m\e[32m$SLEEP sec\e[0m"
echo '================================================='
