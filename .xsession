#!/bin/bash

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# Merge in default and keymaps

if [ -f sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge $userresources
fi

if [ -f "$usermodmap" ]; then
    xmodmap -merge $usermodmap
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ]; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Some shortcuts
sxhkd &
# Set the 100% of brightness
brightnessctl set 100% &
# Image compositor

picom --config ~/.config/picom/picom.conf -b &
# picom --experimental-backend -b &
# Screens

# # Tele a la izquierda
# xrandr --output eDP1 --mode 1366x768 --pos 1920x312 --rotate normal --output DP1 --off --output HDMI1 --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off &

# # Tele arriba
# xrandr --output eDP1 --primary --mode 1366x768 --pos 277x1080 --rotate normal --output DP1 --off --output HDMI1 --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off

# Pantalla chica arriba
xrandr --output eDP1 --primary --mode 1366x768 --pos 0x768 --rotate normal --output DP1 --off --output HDMI1 --mode 1360x768 --pos 6x0 --rotate normal --output VIRTUAL1 --off
# Pantalla chica izquierda
xrandr --output eDP1 --primary --mode 1366x768 --pos 1360x0 --rotate normal --output DP1 --off --output HDMI1 --mode 1360x768 --pos 0x0 --rotate normal --output VIRTUAL1 --off

# Wallpaper
# feh --bg-scale ~/Wallpapers/wallpaper7.jpg &
nitrogen --restore
# Keyboard layout
setxkbmap es && xmodmap ~/.MyKeys && bash /home/shelo/.config/qtile/scripts/toggleKeyboard.sh &

# # Automount devices
# udiskie -t &

# Not enough? Visit this GitHub repository with more:
# https://github.com/antoniosarosi/dotfiles/tree/83fb32e60921a879cfab717553f8f016e0145d2b

alacritty -e bash ~/.updater.sh &
