#! /bin/bash 
lxsession &
picom --config ~/.config/picom/picom.conf &
nitrogen --restore
#picom -CGb &
blueberry-tray &
redshift -O 5000K &
xfce4-clipman &
[ ! -s ~/.config/mpd/pid ] && mpd
sh ~/.config/qtile/scripts/monitor.sh
sh ~/.config/qtile/scripts/battery.sh &
dunst -conf ~/.config/dunst/dunstrc &

