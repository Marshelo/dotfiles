local gears = require('gears')
local awful = require('awful')
local hotkeys_popup = require('awful.hotkeys_popup')
local naughty = require("naughty")

-- Modules
local defaults = require('config.vars.defaults')
local taglist = require('config.vars.taglist')
local shortcut = require('config.modes.shortcut')
local menus = require('config.menus')


-- {{{ Keys
super = 'Mod4'
alt = 'Mod1'
shift = 'Shift'
control = 'Control'

local keys = {}

keys.up = 's'
keys.down = 'z'
keys.left = 'a'
keys.right = 'x'



-- Key bindings

keys.globalkeys = gears.table.join(
    awful.key({ super,           }, 'F5', awesome.restart,
        {description = 'reload awesome', group = 'awesome'}),
    awful.key({ super,           }, 'Delete', awesome.quit,
        {description = 'quit awesome', group = 'awesome'}),

    awful.key({ super }, 'd', shortcut.mode),
    awful.key({ super }, 'k', menus.mymainmenu:show()),

    awful.key({ super,           }, 'F1',      hotkeys_popup.show_help,
              {description='show help', group='awesome'}),
    -- awful.key({ super,           }, 'd', function ()  end,
    --     {description = 'show main menu', group = 'awesome'}),
    awful.key({ super,           }, '?',      hotkeys_popup.show_help,
            {description='show help', group='awesome'}),
    awful.key({ super,           }, 'Left',   awful.tag.viewprev,
              {description = 'view previous', group = 'tag'}),
    awful.key({ super,           }, 'Right',  awful.tag.viewnext,
              {description = 'view next', group = 'tag'}),
    -- awful.key({ super,           }, 'Escape', awful.tag.history.restore,
    --           {description = 'go back', group = 'tag'}),
    -- #############################################################################
    -- Desktop Functions
    -- Sound
    awful.key({ }, 'XF86AudioLowerVolume', function ()
        awful.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%') end),
    awful.key({ }, 'XF86AudioRaiseVolume', function ()
        awful.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%') end),
    awful.key({ }, 'XF86AudioMute', function ()
        awful.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle') end),

    -- Playback
    awful.key({ }, 'XF86AudioPlay', function ()
        awful.spawn('playerctl play-pause') end),
    awful.key({ }, 'XF86AudioPrev', function ()
        awful.spawn('playerctl previous') end),
    awful.key({ }, 'XF86AudioNext', function ()
        awful.spawn('playerctl next') end),

    -- Launcher
    awful.key({super}, 'o', function ()
        awful.spawn('rofi -combi-modi window,drun,ssh -show drun') end,
        {description = 'open launcher', group = 'launcher'}),
    -- Switch windows
    awful.key({alt}, 'Tab', function ()
        awful.spawn('rofi -combi-modi window,drun,ssh -show window -theme ~/.config/rofi/launchers/type-3/style-9.rasi') end,
        {description = 'switch windows', group = 'launcher'}),
    -- #############################################################################


    -- Move focus in layouts
    awful.key({ super,           }, keys.up, function ()
            awful.client.focus.bydirection('up') end,
        {description = 'focus client above', group = 'layout'}),
    awful.key({ super,           }, keys.down, function ()
            awful.client.focus.bydirection('down') end,
        {description = 'focus client below', group = 'layout'}),
    awful.key({ super,           }, keys.left, function ()
            awful.client.focus.bydirection('left') end,
        {description = 'focus left client', group = 'layout'}),
    awful.key({ super,           }, keys.right, function ()
            awful.client.focus.bydirection('right') end,
        {description = 'focus right client', group = 'layout'}),

    -- Layout manipulation
    awful.key({ super, shift     }, keys.up, function () awful.client.swap.bydirection('up')    end,
        {description = 'swap with client above', group = 'layout'}),
    awful.key({ super, shift     }, keys.down, function () awful.client.swap.bydirection('down')    end,
        {description = 'swap with client below', group = 'layout'}),
    awful.key({ super, shift     }, keys.left, function () awful.client.swap.bydirection('left')    end,
        {description = 'swap with left client', group = 'layout'}),
    awful.key({ super, shift     }, keys.right, function () awful.client.swap.bydirection('right')    end,
        {description = 'swap with right client', group = 'layout'}),
    awful.key({ super,           }, 'space',
        function ()
            awful.client.focus.history.previous()
            if client.focus then
                client.focus:raise()
            end
        end,
        {description = 'go back', group = 'client'}),

    awful.key({ super, control   }, keys.up,
        function () awful.tag.incmwfact( 0.05) end,
        {description = 'increase master width factor', group = 'layout'}),
    awful.key({ super, control   }, keys.down,
        function () awful.tag.incmwfact(-0.05) end,
        {description = 'decrease master width factor', group = 'layout'}),
    awful.key({ super, control, shift }, keys.up,
        function () awful.tag.incnmaster( 1, nil, true) end,
        {description = 'increase the number of master clients', group = 'layout'}),
    awful.key({ super, control, shift }, keys.down,
        function () awful.tag.incnmaster(-1, nil, true) end,
        {description = 'decrease the number of master clients', group = 'layout'}),
    awful.key({ super, control   }, keys.left,
        function () awful.tag.incncol( 1, nil, true)    end,
        {description = 'increase the number of columns', group = 'layout'}),
    awful.key({ super, control   }, keys.left,
        function () awful.tag.incncol(-1, nil, true)    end,
        {description = 'decrease the number of columns', group = 'layout'}),
    awful.key({ super,           }, 'Tab', function () awful.layout.inc( 1)                end,
        {description = 'select next', group = 'layout'}),
    awful.key({ super, shift     }, 'Tab', function () awful.layout.inc(-1)                end,
        {description = 'select previous', group = 'layout'}),

    -- Screens manipulation
    awful.key({ super, alt       }, keys.up, function () awful.screen.focus_bydirection('up') end,
        {description = 'focus the screen above', group = 'screen'}),
    awful.key({ super, alt       }, keys.down, function () awful.screen.focus_bydirection('down') end,
        {description = 'focus the screen below', group = 'screen'}),
    awful.key({ super, alt       }, keys.left, function () awful.screen.focus_bydirection('left') end,
        {description = 'focus the left screen', group = 'screen'}),
    awful.key({ super, alt       }, keys.right, function () awful.screen.focus_bydirection('right') end,
        {description = 'focus the right screen', group = 'screen'}),

    -- Prompt
    awful.key({ super,           }, 'p',     function () awful.screen.focused().mypromptbox:run() end,
              {description = 'run prompt', group = 'launcher'})
)

keys.clientkeys = gears.table.join(
    awful.key({ super,           }, 'F11',
        function (c)
            c.fullscreen = not c.fullscreen
            c:raise()
        end,
        {description = 'toggle fullscreen', group = 'client'}),
    awful.key({ super, shift }, 'c',      function (c) c:kill() end,
        {description = 'close', group = 'client'}),
    awful.key({ super, control }, 'f',  awful.client.floating.toggle,
        {description = 'toggle floating', group = 'client'}),
    awful.key({ super, control }, 'Return', function (c) c:swap(awful.client.getmaster()) end,
        {description = 'move to master', group = 'client'}),
    awful.key({ super, shift }, 'i',      function (c) c:move_to_screen() end,
        {description = 'move to screen', group = 'client'}),
    awful.key({ super }, 't',      function (c) c.ontop = not c.ontop end,
        {description = 'toggle keep on top', group = 'client'}),
    awful.key({ super }, 'f',
        function (c)
            -- The client currently has the input focus, so it cannot be
            -- minimized, since minimized clients can't have the focus.
            c.minimized = true
        end ,
        {description = 'minimize', group = 'client'}),
    awful.key({ super, shift }, 'f',
        function ()
            local c = awful.client.restore()
            -- Focus restored client
            if c then
            c:emit_signal(
                'request::activate', 'key.unminimize', {raise = true}
            )
            end
        end,
        {description = 'restore minimized', group = 'client'}),

    awful.key({ super }, 'v',
        function (c)
            c.maximized = not c.maximized
            c:raise()
        end ,
        {description = '(un)maximize', group = 'client'}),
    awful.key({ super, shift }, 'v',
        function (c)
            c.maximized_vertical = not c.maximized_vertical
            c:raise()
        end ,
        {description = '(un)maximize vertically', group = 'client'}),
    awful.key({ super, control }, 'v',
        function (c)
            c.maximized_horizontal = not c.maximized_horizontal
            c:raise()
        end ,
        {description = '(un)maximize horizontally', group = 'client'})
)

-- Bind all keys to tags.
for i = 1, #taglist.settings do
    keys.globalkeys = gears.table.join(keys.globalkeys,
        -- View tag only.
        awful.key({ super }, taglist.settings[i].key,
            function ()
                local screen = awful.screen.focused()
                local tag = screen.tags[i]
                if tag then
                    tag:view_only()
                end
            end,
            {description = 'view tag #'.. taglist.settings[i].key, group = 'tag'}),
        -- Toggle tag display.
        awful.key({ super, control   }, taglist.settings[i].key,
            function ()
                local screen = awful.screen.focused()
                local tag = screen.tags[i]
                if tag then
                    awful.tag.viewtoggle(tag)
                end
            end,
            {description = 'toggle tag #' .. taglist.settings[i].key, group = 'tag'}),
        -- Move client to tag.
        awful.key({ super, shift   }, taglist.settings[i].key,
            function ()
                if client.focus then
                    local tag = client.focus.screen.tags[i]
                    if tag then
                        client.focus:move_to_tag(tag)
                    end
                end
            end,
            {description = 'move focused client to tag #'.. taglist.settings[i].key, group = 'tag'}),
        -- Toggle tag on focused client.
        awful.key({ super, control  , shift   }, taglist.settings[i].key,
            function ()
                if client.focus then
                    local tag = client.focus.screen.tags[i]
                    if tag then
                        client.focus:toggle_tag(tag)
                    end
                end
            end,
            {description = 'toggle focused client on tag #' .. taglist.settings[i].key, group = 'tag'})
    )
end

keys.clientbuttons = gears.table.join(
    awful.button({ }, 1, function (c)
        c:emit_signal('request::activate', 'mouse_click', {raise = true})
    end),
    awful.button({ super }, 1, function (c)
        c:emit_signal('request::activate', 'mouse_click', {raise = true})
        awful.mouse.client.move(c)
    end),
    awful.button({ super }, 3, function (c)
        c:emit_signal('request::activate', 'mouse_click', {raise = true})
        awful.mouse.client.resize(c)
    end)
)

-- Set keys
root.keys(keys.globalkeys)
-- }}}


return keys