from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.utils import guess_terminal

from .groups import groups, videoG, radioG, boardG

from libqtile.log_utils import logger


# Hacer combinación de teclas para mostrar el modo en el que estoy

mod = 'mod4'
alt = 'mod1'
terminal = guess_terminal()


left = 'h'
right = 'l'
up = 'k'
down = 'j'

leftVim = 'h'
downVim = 'j'
upVim = 'k'
rightVim = 'l'


# Main key bindings. In mode.py there is the key bindings for each mode.

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html


    # ------------ Windows Config ------------ #

    # Switch between windows
    Key([mod], left, lazy.layout.left()),
    Key([mod], right, lazy.layout.right()),
    Key([mod], down, lazy.layout.down()),
    Key([mod], up, lazy.layout.up()),
    Key([mod], 'space', lazy.layout.next()),

    # Move windows
    Key([mod, 'shift'], left, lazy.layout.shuffle_left()),
    Key([mod, 'shift'], right, lazy.layout.shuffle_right()),
    Key([mod, 'shift'], down, lazy.layout.shuffle_down()),
    Key([mod, 'shift'], up, lazy.layout.shuffle_up()),
    # Moving out of range in Columns layout will create new column.

    # Grow windows
    Key([mod, 'control', 'shift'], leftVim, lazy.layout.grow_left()),
    Key([mod, 'control', 'shift'], rightVim, lazy.layout.grow_right()),
    
    Key([mod, 'control', 'shift'],downVim,
        lazy.layout.grow_down().when(layout='columns'),
        lazy.layout.shrink().when(layout='monadtall'),
        lazy.layout.shrink().when(layout='monadwide')),
    Key([mod, 'control', 'shift'], upVim,
        lazy.layout.grow_up().when(layout='columns'),
        lazy.layout.grow().when(layout='monadtall'),
        lazy.layout.grow().when(layout='monadwide')),

    # More
    Key(['shift'], 'F11', lazy.window.toggle_fullscreen()),
        
    Key([mod, 'control'], 'space', lazy.layout.flip()),
    Key([mod, 'control'], 'n', lazy.layout.normalize()),

    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),

    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod, 'shift'], 'Tab', lazy.prev_layout()),
    Key([mod], 'c', lazy.window.kill()),
    Key([mod, 'control'], 'f', lazy.window.toggle_floating()),

    # Key([mod], 'F5', lazy.restart()),
    Key([mod], 'F5', lazy.spawn('qtile cmd-obj -o cmd -f restart')), # Change "restart" to "reload_config" if you have the qtile git version.
    Key([mod], 'Delete', lazy.shutdown()),
    
    # Window Edit mode (Basically the same shortcuts but whitout the mod key)
    

    # ------------ App Configs ------------ #

    # Menu
    Key([mod], 'o', lazy.spawn('rofi -modi drun -show drun')),
    Key([mod, 'shift'], 'o', lazy.run_extension(extension.DmenuRun(
        dmenu_font='JetBrainsMono Nerd Font',
        font='JetBrainsMono Nerd Font',
        dmenu_lines=4,
    ))),
    Key([alt], 'Tab', lazy.spawn('rofi -show')),
    # # Menu
    # Key([mod], 'o', lazy.spawn('rofi -modi drun -show drun')),
    # # Window Nav
    # Key([alt], 'Tab', lazy.spawn('rofi -show')),


    # Browser
    Key([mod], 'b', lazy.spawn('firefox')),

    # Terminal
    Key([mod], 'Return', lazy.spawn(terminal)),

    # File manager
    Key([mod], 'f', lazy.spawn('thunar')),

    # Screenshot
    Key([], 'Print', lazy.spawn('scrot -s')),
    Key([mod, 'shift'], 's', lazy.spawn('scrot')),


    # ------------ Widgets Configs ------------ #

    Key([mod], 't', lazy.spawncmd()),
    Key([alt], 'Return', # Toggle keyboard map
        lazy.spawn('bash /home/shelo/.config/qtile/scripts/toggleKeyboard.sh'),
        desc='Toggle keymap beetwen US & Latam keyboard'),


    # ------------ Function Keys ------------ #

    # Volume
    Key([], 'XF86AudioLowerVolume',
        lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%')),
    Key([], 'XF86AudioRaiseVolume',
        lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%')),
    Key([], 'XF86AudioMute',
        lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),

    # Audio control
    Key([], 'XF86AudioPlay',
        lazy.spawn('playerctl play-pause')),
    Key([], 'XF86AudioPrev',
        lazy.spawn('playerctl previous')),
    Key([], 'XF86AudioNext',
        lazy.spawn('playerctl next')),

    Key(['shift'], 'XF86AudioPlay',
        lazy.spawn('playerctl play-pause -p spotify')),
    Key(['shift'], 'XF86AudioPrev',
        lazy.spawn('playerctl previous -p spotify')),
    Key(['shift'], 'XF86AudioNext',
        lazy.spawn('playerctl next -p spotify')),

    # Brightness
    Key([], 'XF86MonBrightnessUp',
        lazy.spawn('brightnessctl set +5%')),
    Key([], 'XF86MonBrightnessDown',
        lazy.spawn('brightnessctl set 5%-')),

    Key([mod], 'p', lazy.spawn('arandr'))
    # I don't facking now what the hell is happening here.
    # The function of the F4 key is red like Super_L + p.
    # So I just putted that keys here and it works, but now
    # if I really press Super_L + p run the same function.
  

]

firstNums = 4 # Just until 9 and no negative numbers
groupKeys = 'qwer' # Leave empty to use only numbers or assign letters to use them for the group's shortcuts.
# Whit this new loop you can assign a shortcut automatically for each group with letters
# The first 8 shortcut are so confortable with {1, 2, 3, 4, q, w, e, r}.
for i, group in enumerate(groups):
    actual_key = ''
    if i < firstNums:
        actual_key = str(i + 1)
    elif i < firstNums + len(groupKeys):
        actual_key = groupKeys[i - 4]
    elif firstNums + len(groupKeys) - 1 < i < 9 + len(groupKeys):
        actual_key = str(i - len(groupKeys) + 1)
    elif i == 9 + len(groupKeys):
        actual_key = '0'
    
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, 'shift'], actual_key, lazy.window.togroup(group.name))
    ])

keys.extend([
        KeyChord([mod], 'm', [
            Key([], 'v', lazy.group[videoG].toscreen()),
            Key([], 'a', lazy.group[radioG].toscreen()),
        ])  
    ])
