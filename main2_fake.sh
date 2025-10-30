#!/bin/bash
echo "Making you invisible to the eyes on the network !!"
sleep 1
cowthink -w "INVISIBILITY CLOAK ACTIVATE !" | lolcat
sleep 1
echo "waking up guards..."
echo "preparing them... "
sleep 2
echo "there we go !"
echo "firewall active" | lolcat
echo "================================" | lolcat


echo "10.201.67.176:8080
10.201.67.176:80
10.201.67.176:443
10.201.67.176:237
10.201.67.176:23
10.201.67.176:98
10.201.67.176:449" | while read line; do
    ip=$(echo $line | awk -F: '{print $1}')
    port=$(echo $line | awk -F: '{print $2}')
    echo "Connection from $ip on port $port" | lolcat
    python3 main.py "$ip" "$port"
    sleep 1
done