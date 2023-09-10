from libqtile import layout
from libqtile.config import Match


layout_conf = {
    'border_focus': '#ff00ff',
    'border_normal': '#000000',
    'border_width': 5,
    'margin': 40 # It doesn't work
}

layouts = [
    layout.Columns(
        border_focus='#ffffff',
        border_normal='#000000',
        border_focus_stack='#909090',
        border_width=2,
        margin=0,
        fair=False,
        margin_on_single=False,
        grow_amount=5, # Default: 10
        wrap_focus_columns=False,
        wrap_focus_rows=False
    ),
    layout.Max(),
    layout.Zoomy(),
    layout.Bsp(
        border_focus='#ffffff',
        border_normal='#000000',
        border_focus_stack='#909090',
        border_width=2,
        margin=0,
        fair=False,
        margin_on_single=False,
        grow_amount=5, # Default: 10
        wrap_focus_columns=False,
        wrap_focus_rows=False),
    # layout.MonadTall(
    #     border_focus='#ffffff',
    #     border_normal='#000000',
    #     ratio=0.6,
    #     change_ratio=0.05,
    #     border_width=2,
    #     margin=0,
    #     single_margin=0,
    #     single_border_width=0
    # ),
    # layout.MonadWide(
    #     border_focus='#ffffff',
    #     border_normal='#000000',
    #     change_ratio=0.05,
    #     border_width=2,
    #     ratio=0.55,
    #     single_margin=0,
    #     single_border_width=0,
    #     min_ratio=0.10,
    #     max_ratio=0.90
    # ),

    # Seguir investigando cuando ocupe 2 pantallas o más.

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
border_focus='#ffffff',
border_normal='#000000',
border_width=0,
)
