#!/bin/bash
echo "#### Installing: "
echo "####    ranger plugins..."
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
git clone https://github.com/maximtrp/ranger-archives.git ~/.config/ranger/plugins/ranger-archives

echo "####    pygmentize..."
sudo pacman -S python-pygments

echo Done