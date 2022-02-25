from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from .keys import mod, alt, left, right, up, down, leftVim, rightVim, upVim, downVim

terminal = guess_terminal


WindowEdit = KeyChord([mod, 'control'], 'e', [
        Key([], 'e', lazy.ungrab_all_chords()),
        # Switch between windows
        Key([], left, lazy.layout.left()),
        Key([], right, lazy.layout.right()),
        Key([], down, lazy.layout.down()),
        Key([], up, lazy.layout.up()),
        Key([], 'space', lazy.layout.next()),
        # Move windows
        Key(['shift'], left, lazy.layout.shuffle_left()),
        Key(['shift'], right, lazy.layout.shuffle_right()),
        Key(['shift'], down, lazy.layout.shuffle_down()),
        Key(['shift'], up, lazy.layout.shuffle_up()),
        # Grow windows
        Key(['control'], leftVim, lazy.layout.grow_left()),
        Key(['control'], rightVim, lazy.layout.grow_right()),
        Key(['control'],downVim,
            lazy.layout.grow_down().when(layout='columns'),
            lazy.layout.shrink()),
        Key(['control'], upVim,
            lazy.layout.grow_up().when(layout='columns'),
            lazy.layout.grow()),
        Key(['control', alt], leftVim, lazy.layout.swap_column_left()),
        Key(['control', alt], rightVim, lazy.layout.swap_column_right()),
        # More control
        Key([], 'space', lazy.layout.flip()),
        Key([], 'n', lazy.layout.normalize()),
        Key([], 'Tab', lazy.next_layout()),
        Key(['shift'], 'Tab', lazy.prev_layout()),
        Key(['shift'], 'Return', lazy.layout.toggle_split()),
        Key([], 'Return', lazy.spawn(terminal)),
        Key([], 'o', lazy.spawn('rofi -modi drun -show drun')),
        Key([], 'q', lazy.window.kill())],
        mode='Window Edit'
    )