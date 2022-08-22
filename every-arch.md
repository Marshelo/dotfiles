# Every Arch

## Drivers and functionalities
### Fonts
- `sudo pacman -S noto-fonts` - To fix fonts problems
- `sudo pacman -S noto-fonts-cjk` - Other languages fonts, but I don't recommend because the Nerd Fonts
- `yay -S ttf-twemoji` - Emojis support

### Others
- `sudo pacman -S wget` - Web downloads
- `sudo pacman -S ntfs-3g` - To read NTFS file system
- `sudo pacman -S pulseaudio` - Audio

### "missing firmware for module: ..."
- `sudo pacman -S linux-firmware-qlogic` - Fix most problems

If modules for aic94xx, wd719x or xhci_pci are still missing execute:
- `yay -S aic94xx-firmware`
- `yay -S wd719x-firmware`
- `yay -S upd72020x-fw`

Respectively

## Tools
### Sound
- `sudo pacman -S pavucontrol` - Mixer
### File manager
- `sudo pacman -S ranger` - Terminal file manager (The best I think)
- `sudo pacman -S ueberzug` - Ranger images previews support at most terminals
- `sudo pacman -S poppler` - Ranger PDFs previews support
### Screen
`sudo pacman -S arandr` - Generates a command for your own screens configurations
- `sudo pacman -S redshift libnotify notification-daemon cbatticon network-manager-applet` - For blue light suppression
- `sudo pacman -S vlc` - Media player

## Personalization
`curl -sS https://starship.rs/install.sh | sh` - One very custom prompt for any shell
- `sudo pacman -S fish`
- `sudo chsh -s /usr/local/bin/fish` - Makes fish as default shell
- `sudo pacman -S alacritty` - GPU acelereted term
- `sudo pacman -S kitty` - GPU based term
- Install kitty-cat and change the default themes folder from /bin/kitty-cat and put "~/.config/kitty/themes"
```bash
mkdir -p ~/installing || cd ~/installing
git clone https://github.com/adi1090x/kitty-cat.git || bash ./kitty-cat/install
```

