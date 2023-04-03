# With this key bindings I pretend to have the power of the keyboard and the power of the mouse
# synchronized for work with every thing. For that I had to found the way to work in the keyboard
# just with the left hand for leave free my right hand only for the mouse. And I founded the way
# and is very efficient.
# Actually I have to move the right hand to the keyboard for some commands, but only if I will
# write or do more complex key combinations.


from libqtile import extension
import libqtile
from libqtile.config import Key, KeyChord, Screen
from libqtile.command import lazy
from libqtile.backend.base import Window

from .groups import groups, separator

browser = 'brave'
terminal = 'kitty'
# terminal = 'alacritty'

# If something happend, see the default commands here
# https://docs.qtile.org/en/latest/manual/config/lazy.html

# Hacer combinación de teclas para mostrar el modo en el que estoy

super = 'mod4' # Super key
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


# from libqtile.command.client import InteractiveCommandClient
# c = InteractiveCommandClient()

keys = [
    # ------------ WINDOWS ------------ #

    Key([super], 'space', lazy.screen.toggle_group()),
    # Key([mod], 'space', c.group["sep1"].to_screen(0)),

    # Switch between windows
    Key([super], left, lazy.layout.left()),
    Key([super], down, lazy.layout.down()),
    Key([super], up, lazy.layout.up()),
    Key([super], right, lazy.layout.right()),
    # Key([mod], 'space', lazy.layout.next()),

    # Move windows
    Key([super, 'shift'], left, lazy.layout.shuffle_left()),
    Key([super, 'shift'], down, lazy.layout.shuffle_down()),
    Key([super, 'shift'], up, lazy.layout.shuffle_up()),
    Key([super, 'shift'], right, lazy.layout.shuffle_right()),

    # Grow windows
    Key([super, 'control'], left, lazy.layout.grow_left()),
    Key([super, 'control'], right, lazy.layout.grow_right()),

    Key([super, 'control'], down,
        lazy.layout.grow_down().when(layout='columns'),
        lazy.layout.shrink().when(layout='monadtall'),
        lazy.layout.shrink().when(layout='monadwide')),
    Key([super, 'control'], up,
        lazy.layout.grow_up().when(layout='columns'),
        lazy.layout.grow().when(layout='monadtall'),
        lazy.layout.grow().when(layout='monadwide')),

    # More
    Key([super], 'F11', lazy.window.toggle_fullscreen()),

    Key([super, 'control'], 'space', lazy.layout.flip()),
    Key([super, 'control'], 'n', lazy.layout.normalize()),

    Key([super, 'shift'], 'space', lazy.layout.toggle_split()),

    Key([super], 'Tab', lazy.next_layout()),
    Key([super, 'shift'], 'Tab', lazy.prev_layout()),
    Key([super, 'shift'], 'c', lazy.window.kill()),
    Key([super, 'control'], 'f', lazy.window.toggle_floating()),

    # Key([mod], 'F5', lazy.restart()),
    Key([super], 'F5', lazy.spawn('qtile cmd-obj -o cmd -f restart')), # Change "restart" to "reload_config" if you have the qtile git version.
    Key([super], 'Delete', lazy.shutdown()),

    # ------------ DESKTOP FUNCTIONS ------------ #
    # SOUND
    # Volume
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),

    # Playback
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next')),


    # Launcher
    Key([super], 'o', lazy.spawn('rofi -combi-modi window,drun,ssh -show drun')),
    # Smitch windows
    Key([alt], 'Tab', lazy.spawn('rofi -combi-modi window,drun,ssh -show window -theme ~/.config/rofi/launchers/type-3/style-9.rasi')),

    # Widget cmd line
    Key([super], 'p', lazy.spawncmd()),

    Key([super, alt], 'h', lazy.hide_show_bar("bottom")),
]


first_nums = 3
group_keys = 'qwe'
sep = 0
for i, group in enumerate(groups):

    current_key = ''
    ii = i - sep
    # the ii var back the i value to his natural course after adding a separator
    # because the separator is actually another group but I skip it whit this if
    # statement below to don't add any shortcut to it.
    if group.label == separator:
        sep += 1
        # if sep == 2:
        #     break
        continue

    if sep < 3:
        if ii < first_nums:
            current_key = str(i + 1)
        elif ii < first_nums + len(group_keys):
            current_key = group_keys[ii - len(group_keys)]
        elif first_nums + len(group_keys) - 1 < ii < 9 + len(group_keys):
            current_key = str(ii - len(group_keys) + 1)
        elif ii == 9 + len(group_keys):
            current_key = '0'

    if not current_key == '':
        keys.extend([
            Key([super], current_key, lazy.group[group.name].toscreen()),
            Key([super, 'shift'], current_key, lazy.window.togroup(group.name))
        ])
