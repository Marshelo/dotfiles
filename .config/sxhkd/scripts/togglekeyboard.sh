#!/bin/bash

layout=`setxkbmap -query | grep layout | sed "s/  */ /g" | cut -d " " -f 2`

if [[ $layout = "us" ]]
then
    if [[ -f ~/.MyKeys ]]
    then
        setxkbmap es && xmodmap ~/.MyKeys
    else
        setxkbmap latam
    fi
fi

if [[ $layout = "es" ]]
then
    setxkbmap latam
fi
if [[ $layout = "latam" ]]
then
    setxkbmap us
fi

echo Comandos ejecutados