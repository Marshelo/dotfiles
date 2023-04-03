from libqtile.config import Click, Drag
from libqtile.command import lazy

from .keys import super, alt

# Drag floating layouts.
mouse = [
    Drag([super], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([super], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([super], 'Button2', lazy.window.bring_to_front())
]