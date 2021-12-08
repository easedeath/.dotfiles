#! /bin/bash 
lxsession &
picom --config ~/.config/picom/picom.conf &
nitrogen --restore &
blueberry-tray &
redshift -O 5000K &
xfce4-clipman &
bash ~/.config/qtile/scripts/monitor.sh &
bash ~/.config/qtile/scripts/battery.sh &
dunst -conf ~/.config/dunst/dunstrc &
