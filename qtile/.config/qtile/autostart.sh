#! /bin/bash
lxsession &
picom --config ~/.config/picom/picom.conf &
xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'& # Caps_Lock is annoying
nitrogen --restore &
blueberry-tray &
redshift -O 5000K &
xfce4-clipman &
bash ~/.config/qtile/scripts/monitor.sh &
bash ~/.config/qtile/scripts/battery.sh &
dunst -conf ~/.config/dunst/dunstrc &
