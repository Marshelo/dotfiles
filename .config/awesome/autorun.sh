#!/bin/sh

run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

pkill volctl
pkill cbatticon
pkill udiskie
pkill nm-applet

volctl &
cbatticon &
udiskie -t &
nm-applet &