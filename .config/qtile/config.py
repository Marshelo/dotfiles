# Settings
from settings.keys import keys
from settings.mouse import mouse
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import screens


from os import path
import subprocess
from settings.path import qtile_path
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

from libqtile import utils
utils.guess_terminal = 'alacritty'

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
auto_minimize = True # When applications want... like steam games
wmname = 'LG3D'
