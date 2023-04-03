from libqtile import bar, widget, command
from libqtile.config import Screen
from .groups import space
from libqtile.command import lazy
from libqtile import qtile
from .palette import colors as color

os_icon = '   '

widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    #font='UbuntuMono Nerd Font',
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()

def triangle(fg='#ffffff', bg='#000000', direction='left', shadow=None):
    triangle=''
    if direction == 'left':
        triangle = ''
    elif direction == 'right':
        triangle = ' '
        # 
    return widget.TextBox(
        text=triangle,
        font='JetBrainsMono Nerd Font',
        fontsize=43,
        padding=-5,
        background=bg,
        foreground=fg,
        fontshadow=shadow
    )

def display_groups(visible=[], hide_unused=False, fg='#ff00ff', bg='#00ffff', highlight='#ffff00', active='#ff00ff', inactive='#00ffff', screen='#0000ff'):
    return widget.GroupBox(
        # ~~ Frame ~~
        # Text
        font='FreeSans', # This keep the icons where it goes
        fontsize=32,
        margin=10,
        margin_y=4,
        margin_x=0,
        spacing=None,
        center_aligned=True,
        # Selector
        highlight_method='line',
        padding_y=5,
        padding_x=5,
        borderwidth=5,
        # ~~ Color ~~
            background=bg,
            # Text
            this_current_screen_border=screen,
            this_screen_border='#0025a0',
            other_current_screen_border='#008015',
            other_screen_border='#008015',
            block_highlight_text_color=fg,
            active=active,
            inactive=inactive,
            # Selector
            highlight_color=highlight,
        # ~~ Extra ~~
        disable_drag=True,
        visible_groups=visible,
        hide_unused=hide_unused
    )

widget_box = widget.WidgetBox(widgets=[
                    widget.TextBox(text="CPU", foreground='#000000', background=color['gray3'], font='Ubuntu NF'),
                    widget.CPUGraph(
                        margin_y=0,
                        margin_x=0,
                        border_color=color['gray3'],
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=color['gray3'],
                        # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="RAM", foreground='#000000', background=color['gray3'], font='Ubuntu NF'),
                    widget.MemoryGraph(
                        margin_y=0,
                        margin_x=0,
                        border_color=color['gray3'],
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=color['gray3'],
                        # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="DISC", foreground='#000000', background=color['gray3'], font='Ubuntu NF'),
                    widget.HDDBusyGraph(
                        margin_y=0,
                        margin_x=0,
                        border_color=color['gray3'],
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=color['gray3'],
                        # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="NET", foreground='#000000', background=color['gray3'], font='Ubuntu NF'),
                    widget.NetGraph(
                        margin_y=0,
                        margin_x=0,
                        border_color=color['gray3'],
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=color['gray3'],
                        # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    ],
                    close_button_location='right',
                    font='JetBrainsMono Nerd Font',
                    fontsize='24',
                    foreground=color['black'],
                    center_aligned=False,
                    text_open=' 﫵 ',
                    text_closed='  﫵 ',
                    background=color['gray3'],
                    mouse_callbacks = {'Button2': lambda: qtile.cmd_spawn('alacritty -e htop')}
                )

foo = widget.Systray(padding=5)

def toggleBox(qtile):
    widget_box.cmd_toggle()
    print('conshesumare AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print(foo.Icon.icon_size)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox(
                    text=os_icon,
                    font='JetBrainsMono Nerd Font',
                    fontsize=20,
                    padding=7,
                    foreground=color['gray2'],
                    background=color['bg'],
                    fontshadow='#101010',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('rofi -combi-modi window,drun,ssh -show window -theme ~/.config/rofi/launchers/type-3/style-9.rasi')}
                ),
                triangle(color['bg'], color['gray3'], 'right', shadow='#101010'),
                display_groups([space[0], space[1], space[2]],
                    bg=color['gray3'],
                    fg=color['almost black'],
                    active=color['gray1'],
                    inactive=color['gray2'],
                    highlight=color['gray3'],
                    screen=color['screen1b'],
                    hide_unused=True
                ),
                triangle(color['gray3'], color['bg'], 'right', shadow='#000000'),
                display_groups([space[3], space[4], space[5]],
                    fg=color['fg'],
                    bg=color['bg'],
                    active=color['gray2'],
                    inactive=color['gray0'],
                    highlight=color['bg'],
                    screen=color['screen1a']
                ),
                triangle(color['bg'], color['gray3'], 'right', shadow='#101010'),
                display_groups([space[6], space[7], space[8]],
                    bg=color['gray3'],
                    fg=color['almost black'],
                    active=color['gray1'],
                    inactive=color['gray2'],
                    highlight=color['gray3'],
                    screen=color['screen1b'],
                    hide_unused=True
                ),
                triangle(color['gray3'], color['bg'], 'right', shadow='#0a0a0a'),
                # widget.Spacer(length=20),
                widget.CurrentLayoutIcon(foreground=color['white'], scale=0.8, padding=20 ),
                # widget.WindowCount(font='UbuntuMono NF Bold'),
                widget.Prompt(
                    font='Your Doodle Font',
                    fontsize=15,
                    padding=0,
                    prompt='>_ ',
                    fmt='{} \\',
                    foreground=color['almost white'],
                    cursor_color=color['almost white'],
                    background=color['bg'],
                    # fontshadow='#000000',
                    cursorblink=0.3,
                    ignore_dups_history=True,
                    record_history=False,
                    visual_bell_time=1,
                    bell_style=None
                ),
                widget.WindowName(
                    font='Ubuntu NF Bold',
                    foreground=color['white'],
                    fontsize=13,
                    padding=100,
                    max_chars=40
                ),
                widget.TextBox(
                    text='',
                    font='ComicSans',
                    fontsize=28,
                    padding=0,
                    foreground=color['gray3'],
                    background=None,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_function(toggleBox), 'Button2': lambda: qtile.cmd_spawn('alacritty -e htop')}
                ),
                widget_box,
                widget.TextBox(
                    text=' ',
                    font='ComciSans',
                    fontsize=28,
                    padding=0,
                    foreground=color['gray3'],
                    fontshadow='#000000',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_function(toggleBox), 'Button2': lambda: qtile.cmd_spawn('alacritty -e htop')}
                ),
                widget.Sep(),
                # widget.Spacer(length=51),
                # widget.Spacer(),
                foo,
                widget.Spacer(length=10),
                # widget.Wlan(),
                # widget.Net(),
                widget.TextBox(
                    text='',
                    font='sans',
                    fontsize=20,
                    # background='#dddddd',
                ),
                widget.KeyboardLayout(
                    font='UbuntuMono Nerd Font',
                    configured_keyboards=['us', 'es', 'latam']
                ),
                widget.TextBox(
                    text='',
                    font='sans',
                    fontsize=20,
                    # background='#dddddd',
                ),
                widget.CheckUpdates(
                    font='UbuntuMono Nerd Font',
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                widget.Spacer(length=10),
                # widget.CapsNumLockIndicator(),
                widget.Sep(),
                widget.Clock(
                    font='Ubuntu NF Bold',
                    format='%H:%M %a %d/%m/%Y',
                    foreground=color['white'],
                    # background='#bfbfbf',
                    padding=10
                ),
            ],
            30,
            opacity=1,
            margin=0,
            background='#21252B',
            border_width=[4, 0, 4, 0],  # Draw top and bottom borders
            border_color=[color['bg'], '000000', color['bg'], '000000']  # Borders are magenta
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox(
                    text=os_icon,
                    font='JetBrainsMono Nerd Font',
                    fontsize=20,
                    padding=7,
                    foreground=color['gray2'],
                    background=color['bg'],
                    fontshadow='#101010'
                    # mouse_callbacks = {'Button1': lambda: qtile.cmd_function(toggleBox)}
                ),
                triangle(color['bg'], color['gray3'], 'right', shadow='#101010'),
                display_groups([space[0], space[1], space[2]],
                    bg=color['gray3'],
                    fg=color['almost black'],
                    active=color['gray1'],
                    inactive=color['gray2'],
                    highlight=color['gray3'],
                    screen=color['screen1b'],
                    hide_unused=True
                ),
                triangle(color['gray3'], color['bg'], 'right', shadow='#000000'),
                display_groups([space[3], space[4], space[5]],
                    fg=color['fg'],
                    bg=color['bg'],
                    active=color['gray2'],
                    inactive=color['gray0'],
                    highlight=color['bg'],
                    screen=color['screen1a']
                ),
                triangle(color['bg'], color['gray3'], 'right', shadow='#101010'),
                display_groups([space[6], space[7], space[8]],
                    bg=color['gray3'],
                    fg=color['almost black'],
                    active=color['gray1'],
                    inactive=color['gray2'],
                    highlight=color['gray3'],
                    screen=color['screen1b'],
                    hide_unused=True
                ),
                triangle(color['gray3'], color['bg'], 'right', shadow='#0a0a0a'),
                # widget.Spacer(length=20),
                widget.CurrentLayoutIcon(foreground=color['white'], scale=0.8, padding=20 ),
                # widget.WindowCount(font='UbuntuMono NF Bold'),
                widget.Prompt(
                    font='Your Doodle Font',
                    fontsize=15,
                    padding=0,
                    prompt='>_ ',
                    fmt='{} \\',
                    foreground=color['almost white'],
                    cursor_color=color['almost white'],
                    background=color['bg'],
                    # fontshadow='#000000',
                    cursorblink=0.3,
                    ignore_dups_history=True,
                    record_history=False,
                    visual_bell_time=1,
                    bell_style=None
                ),
                widget.Spacer(length=10),
                widget.WindowName(
                    font='Ubuntu NF Bold',
                    foreground=color['white'],
                    fontsize=13,
                    padding=100,
                    max_chars=40
                ),
                # widget.CapsNumLockIndicator(),
                widget.Sep(),
                widget.Clock(
                    font='Ubuntu NF Bold',
                    format='%H:%M %a %d/%m/%Y',
                    foreground=color['white'],
                    # background='#bfbfbf',
                    padding=10
                ),
            ],
            30,
            opacity=1,
            margin=0,
            background='#21252B',
            border_width=[4, 0, 4, 0],  # Draw top and bottom borders
            border_color=[color['bg'], '000000', color['bg'], '000000']  # Borders are magenta
        ),
    ),
]
