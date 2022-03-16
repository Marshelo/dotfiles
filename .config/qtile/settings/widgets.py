from libqtile import bar, widget
from libqtile.config import Screen
from .groups import space1, space2, space3, space4, space5, space6, space7, space8, space9

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
        # 
    return widget.TextBox(
        text=triangle,
        font='JetBrainsMono Nerd Font',
        fontsize=35,
        padding=-4,
        background=bg,
        foreground=fg
    )

def display_groups(visible=[], hide_unused=False, fg='#bbbbbb', bg='#000000', highlight='#ffffff', active='#bbbbbb', inactive='#000000'):
    return widget.GroupBox(
        # ~~ Frame ~~
        # Text
        font='FreeSans', # This keep the icons where it goes
        fontsize=28,
        margin=10,
        margin_y=2.4,
        margin_x=0,
        spacing=None,
        center_aligned=True,
        # Selector
        highlight_method='line',
        padding_y=5,
        padding_x=10,
        borderwidth=3,
        # ~~ Color ~~
            background=bg,
            # Text
            this_current_screen_border='#0025a0',
            this_screen_border='#0025a0',
            other_current_screen_border='#800015',
            other_screen_border='#800015',
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

screens = [
    Screen(
        bottom=bar.Bar(
            [
                display_groups([space1, space2, space3], bg='#454545', highlight='#454545'),
                triangle('#454545', '#ffffff', 'right'),
                display_groups([space4, space5, space6], bg='#ffffff', hide_unused=False, highlight='#ffffff'),
                triangle('#ffffff', '#454545', 'right'),
                display_groups([space7, space8, space9], hide_unused=False, bg='#454545', highlight='#454545'),
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
    Screen(
        top=bar.Bar(
            [
                display_groups([space1, space2, space3], bg='#454545', highlight='#454545'),
                triangle('#454545', '#ffffff', 'right'),
                display_groups([space4, space5, space6], bg='#ffffff', highlight='#ffffff'),
                triangle('#ffffff', '#454545', 'right'),
                display_groups(['usual1', 'usual2', 'usual3', 'usual4'], hide_unused=True, bg='#454545', highlight='#454545'),
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
