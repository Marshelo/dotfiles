from libqtile import bar, widget, command
from libqtile.config import Screen
from .groups import space
from libqtile.command import lazy
from libqtile import qtile

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
        triangle = ''
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
colors = {
    'bg': '#21252B', 'fg': '#fafafa',
    'gray1': '#282C34', 'gray2': '#c5c5c5', 'gray3': '#d7dae0',
    'almost white': '#dddddd', 'white': '#ffffff',
    'black': '#000000',
    'screen1a': '#6759ff', 'screen1b': '#0637a0'
    }

widget_box = widget.WidgetBox(widgets=[
                    widget.TextBox(text="CPU", foreground='#000000', background=colors['gray3']),
                    widget.CPUGraph(
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=colors['gray3'],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="RAM", foreground='#000000', background=colors['gray3']),
                    widget.MemoryGraph(
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=colors['gray3'],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="DISC", foreground='#000000', background=colors['gray3']),
                    widget.HDDBusyGraph(
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=colors['gray3'],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    widget.TextBox(text="NET", foreground='#000000', background=colors['gray3']),
                    widget.NetGraph(
                        device='sda',
                        type='linefill',
                        line_width=1,
                        background=colors['gray3'],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                    ),
                    ],
                    close_button_location='right',
                    font='JetBrainsMono Nerd Font',
                    fontsize='24',
                    foreground=colors['black'],
                    center_aligned=False,
                    text_open=' ',
                    text_closed=' ',
                    background=colors['gray3']
                )

def toggleBox(qtile):
    widget_box.cmd_toggle()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                display_groups([space[0], space[1], space[2]],
                    fg=colors['fg'],
                    bg=colors['gray1'],
                    active=colors['gray2'],
                    highlight=colors['gray1'],
                    screen=colors['screen1a'],
                    hide_unused=True
                ),
                triangle(colors['gray1'], colors['gray3'], 'right', shadow='#0a0a0a'),
                display_groups([space[3], space[4], space[5]],
                    bg=colors['gray3'],
                    fg=colors['black'],
                    active=colors['gray1'],
                    inactive=colors['gray2'],
                    highlight=colors['gray3'],
                    screen=colors['screen1b']
                ),
                triangle(colors['gray3'], colors['gray1'], 'right', shadow='#000000'),
                display_groups([space[6], space[7], space[8]],
                    fg=colors['fg'],
                    bg=colors['gray1'],
                    active=colors['gray2'],
                    highlight=colors['gray1'],
                    screen=colors['screen1a'],
                    hide_unused=True
                ),
                triangle(colors['gray1'], colors['bg'], 'right', shadow='#0a0a0a'),
                # widget.Spacer(length=20),
                widget.CurrentLayoutIcon(foreground=colors['white'], scale=0.8, padding=20 ),
                # widget.WindowCount(font='UbuntuMono NF Bold'),
                widget.Prompt(
                    font='JetBrainsMono Nerd Font',
                    fontsize=15,
                    padding=40,
                    prompt=' ',
                    foreground=colors['almost white'],
                    cursor_color=colors['almost white'],
                    background=colors['bg'],
                    # fontshadow='#000000',
                    cursorblink=0.3,
                    ignore_dups_history=True,
                    record_history=False,
                    visual_bell_time=1,
                ),
                widget.WindowName(
                    font='UbuntuMono NF Bold',
                    foreground=colors['white'],
                    fontsize=11,
                    padding=100,
                    max_chars=40
                ),
                widget.TextBox(
                    text='',
                    font='JetBrainsMono Nerd Font',
                    fontsize=26.5,
                    padding=0,
                    foreground=colors['gray3'],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_function(toggleBox)}
                ),
                widget_box,
                widget.TextBox(
                    text='',
                    font='JetBrainsMono Nerd Font',
                    fontsize=26,
                    padding=0,
                    marginx=5,
                    foreground=colors['gray3'],
                    fontshadow='#000000',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_function(toggleBox)}
                ),
                widget.TextBox(text=' ', padding=5),
                widget.Sep(),
                # widget.Spacer(length=51),
                # widget.Spacer(),
                widget.Systray(padding=5,),
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
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                widget.Spacer(length=10),
                # widget.CapsNumLockIndicator(),
                widget.Sep(),
                widget.Clock(
                    format='%H:%M %a %d/%m/%Y',
                    foreground=colors['white'],
                    # background='#bfbfbf',
                    padding=10
                ),
            ],
            30,
            opacity=1,
            margin=0,
            background='#21252B',
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=['ff00ff', '000000', 'ff00ff', '000000']  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                display_groups([space[0], space[1], space[2]], bg='#454545', highlight='#454545'),
                triangle('#454545', '#ffffff', 'right'),
                display_groups([space[3], space[4], space[5]], bg='#ffffff', hide_unused=True, highlight='#ffffff'),
                triangle('#ffffff', '#454545', 'right'),
                display_groups([space[6], space[7], space[8]], hide_unused=True, bg='#454545', highlight='#454545'),
                triangle('#454545', '#000000', 'right'),
                # widget.Spacer(length=20),
                widget.CurrentLayoutIcon( scale=0.8, padding=20 ),
                # widget.WindowCount(font='UbuntuMono NF Bold'),
                widget.Prompt(
                    font='JetBrainsMono Nerd Font',
                    fontsize=15,
                    padding=40,
                    prompt=' : ',
                    foreground='#ffffff',
                    cursor_color='#ffffff',
                    background='#222222',
                    #fontshadow='#000000',
                    cursorblink=0.3,
                    ignore_dups_history=True,
                    record_history=False,
                    visual_bell_time=1,
                ),
                widget.WindowName(
                    font='UbuntuMono NF Bold',
                    fontsize=11,
                    padding=100,
                    max_chars=40
                ),
                # widget.Spacer(length=51),
                # widget.Spacer(),
                widget.Systray(padding=5,),
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
                    font='UbuntuMono Nerd Font'
                ),
                widget.TextBox(
                    text='',
                    font='sans',
                    fontsize=20,
                    # background='#dddddd',
                ),
                widget.CheckUpdates(
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                widget.Spacer(length=10),
                # widget.CapsNumLockIndicator(),
                widget.Sep(),
                widget.Clock(
                    format='%H:%M %a %d/%m/%Y',
                    foreground='#ffffff',
                    # background='#bfbfbf',
                    padding=10
                ),
            ],
            24,
            opacity=0.95,
            margin=0,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=['ff00ff', '000000', 'ff00ff', '000000']  # Borders are magenta
        ),
    ),
]
