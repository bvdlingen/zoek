#!/usr/bin/env bash

echo downloading | lolcat
sudo curl -o /usr/bin/zoek https://raw.githubusercontent.com/bvdlingen/zoek/master/zoek

echo set execute permissions | lolcat
sudo chmod +x /usr/bin/zoek
