from libqtile import bar, widget
from libqtile.config import Screen


widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    #font='UbuntuMono Nerd Font',
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()

def triangle(fg='#ffffff', bg='#000000', direction='left'):
    triangle=''
    if direction == 'left':
        triangle = ''
    elif direction == 'right':
        triangle = ''
    return widget.TextBox(
        text=triangle,
        font='JetBrainsMono Nerd Font',
        fontsize=35,
        padding=-4,
        background=bg,
        foreground=fg
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    # ~~ Frame ~~
                    # Text
                    font='FreeSans', # This keep the icons where it goes
                    fontsize=28,
                    margin=10,
                    margin_y=2.4,
                    margin_x=0,
                    spacing=None,
                    # Selector
                    highlight_method='line',
                    padding_y=5,
                    padding_x=10,
                    borderwidth=0,
                    # ~~ Color ~~
                    # Text
                    block_highlight_text_color='#ffffff',
                    active='#bbbbbb',
                    # Selector
                    highlight_color='#0055ff',
                    # ~~ Extra ~~
                    disable_drag=True,

                ),
                # triangle('#454545', '#ffffff', 'right'),
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
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    # ~~ Frame ~~
                    # Text
                    font='FreeSans', # This keep the icons where it goes
                    fontsize=28,
                    margin=10,
                    margin_y=2.4,
                    margin_x=0,
                    spacing=None,
                    # Selector
                    highlight_method='line',
                    padding_y=5,
                    padding_x=10,
                    borderwidth=0,
                    # ~~ Color ~~
                    # Text
                    block_highlight_text_color='#ffffff',
                    active='#bbbbbb',
                    # Selector
                    highlight_color='#0055ff',
                    # ~~ Extra ~~
                    disable_drag=True,

                ),
                widget.CurrentLayoutIcon( scale=0.8, padding=20 ),
                widget.Prompt(
                    font='JetBrainsMono Nerd Font',
                    fontsize=15,
                    padding=40,
                    prompt=' : ',
                    foreground='#ffffff',
                    cursor_color='#ffffff',
                    background='#222222',
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
                widget.Spacer(length=10),
                widget.TextBox(
                    text='',
                    font='sans',
                    fontsize=20,
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
