# With this key bindings I pretend to have the power of the keyboard and the power of the mouse
# synchronized for work with every thing. For that I had to found the way to work in the keyboard
# just with the left hand for leave free my right hand only for the mouse. And I founded the way
# and is very efficient.
# Actually I have to move the right hand to the keyboard for some commands, but only if I will
# write or do more complex key combinations.  


from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy

from .groups import groups, videoG, radioG, boardG, separator

# If something happend, see the default commands here
# https://docs.qtile.org/en/latest/manual/config/lazy.html

# Hacer combinación de teclas para mostrar el modo en el que estoy

mod = 'mod4' # Super key
alt = 'mod1'

# -- Logic for the modifier keys --
# Super key:
#   Starts all the keybindings for qtile, for differentiate with the commands of the opened applications.
# Shift:
#   When there is already a keybinding for a command, this key toggle the function to its inverse or just change
#   the main functionality.
#   Shift also can have original keybindings but if is combined with another modifier key, bisides the super key.
# Control:
#   This key is just for original keybindings.
#   It's used for grow windows and run special commands.
# Alt:
#   I reserve this key for windows tasks, except for move and grow windows (for comfort).


# I realized that thumb on super key and the other fingers on w, a, s and d is a very bad position for the
# articulations of my thumb. So I replaced w, a, s, d for s, a, z, x, respectively for decrease bad effects.
left = 'a'
down = 'z'
up = 's'
right = 'x'

# These are if I want to do keybindings like vim
leftVim = 'h'
downVim = 'j'
upVim = 'k'
rightVim = 'l'

terminal = 'alacritty'

keys = [
    # ------------ Windows ------------ #

    # Switch between windows
    Key([mod], left, lazy.layout.left()),
    Key([mod], down, lazy.layout.down()),
    Key([mod], up, lazy.layout.up()),
    Key([mod], right, lazy.layout.right()),
    Key([mod], 'space', lazy.layout.next()),

    # Move windows
    Key([mod, 'shift'], left, lazy.layout.shuffle_left()),
    Key([mod, 'shift'], down, lazy.layout.shuffle_down()),
    Key([mod, 'shift'], up, lazy.layout.shuffle_up()),
    Key([mod, 'shift'], right, lazy.layout.shuffle_right()),

    # Grow windows
    Key([mod, 'control', 'shift'], leftVim, lazy.layout.grow_left()),
    Key([mod, 'control', 'shift'], rightVim, lazy.layout.grow_right()),
    
    Key([mod, 'control', 'shift'], downVim,
        lazy.layout.grow_down().when(layout='columns'),
        lazy.layout.shrink().when(layout='monadtall'),
        lazy.layout.shrink().when(layout='monadwide')),
    Key([mod, 'control', 'shift'], upVim,
        lazy.layout.grow_up().when(layout='columns'),
        lazy.layout.grow().when(layout='monadtall'),
        lazy.layout.grow().when(layout='monadwide')),

    # More
    Key([mod], 'F11', lazy.window.toggle_fullscreen()),
        
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

    # ------------ Desktop Apps ------------ #

    # Menu
    Key([mod], 'o', lazy.spawn('rofi -modi drun -show drun')),
    Key([mod, 'shift'], 'o', lazy.run_extension(extension.DmenuRun(
        dmenu_font='JetBrainsMono Nerd Font', dmenu_lines=4))),
    Key([alt], 'Tab', lazy.spawn('rofi -show')),

    # Widget cmd line
    Key([mod], 'p', lazy.spawncmd()),

    # Screenshot
    Key([], 'Print', lazy.spawn('scrot -s')),
    Key(['shift'], 'Print', lazy.spawn('scrot')),

    # ------------ Open Apps ------------ #

    # Browser
    Key([mod], 'b', lazy.spawn('firefox')),
    Key([mod, 'shift'], 'b', lazy.spawn('qutebrowser')),

    # Terminal
    Key([mod], 'Return', lazy.spawn(terminal)),

    # File manager
    Key([mod], 't', lazy.spawn('thunar')),

    # ------------ ?? ------------ #

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

    Key([mod], 'F4', lazy.spawn('arandr')),
]
# cambiar nombre variable actual_key a current_key

first_nums = 3
group_keys = 'qwe'
common_first_nums = 1
common_group_keys = 'r'
sep = 0
for i, group in enumerate(groups):

    current_key = ''
    ii = i - sep
    # the ii var back the i value to his natural course after adding a separator
    # because the separator is actually another group but I skip it whit this if
    # statement below to don't add any shortcut to it.
    if group.label == separator:
        sep += 1
        continue

    if sep < 2:
        if ii < first_nums:
            current_key = str(ii + 1)
        elif ii < first_nums + len(group_keys):
            current_key = group_keys[ii - first_nums]
        # elif first_nums + len(group_keys) - 1 < ii < 9 + len(group_keys):
        #     current_key = str(ii - len(group_keys) + 1)
        # elif ii == 9 + len(group_keys):
        #     current_key = '0'
    if sep == 2:
        if ii - first_nums - len(group_keys) < common_first_nums:
            current_key = str(ii - len(group_keys) + 1)
        # elif ii < first_nums + len(group_keys):
        #     current_key = group_keys[ii - len(group_keys)]
        # elif first_nums + len(group_keys) - 1 < ii < 9 + len(group_keys):
        #     current_key = str(ii - len(group_keys) + 1)
        # elif ii == 9 + len(group_keys):
        #     current_key = '0'
    
    if not current_key == '':
        keys.extend([
            Key([mod], current_key, lazy.group[group.name].toscreen()),
            Key([mod, 'shift'], current_key, lazy.window.togroup(group.name))
        ])

keys.extend([
        KeyChord([mod], 'm', [
            Key([], 'v', lazy.group[videoG].toscreen()),
            Key([], 'a', lazy.group[radioG].toscreen()),
        ])  
    ])
