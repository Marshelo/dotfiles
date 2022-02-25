#!/bin/bash

layout=`setxkbmap -query | grep layout | sed "s/  */ /g" | cut -d " " -f 2`

if [[ $layout = "us" ]]
then
    setxkbmap latam
fi

if [[ $layout = "latam" ]]
then
    setxkbmap us
fi

echo Comandos ejecutados