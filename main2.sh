#!/bin/bash
echo "Making you invisible to the eyes on the network !!"
sleep 1
echo "INVISIBILITY CLOAK ACTIVATE !" 
sleep 1
echo "waking up guards..."
echo "preparing them... "
sleep 2
echo "there we go !"
echo "firewall active" 
echo "===============================" 

while true; do 
	netstat -tn | grep ESTABLISHED | awk '{print $5}' | awk -F: '{print $1, $2}'
	sleep 2 
done
