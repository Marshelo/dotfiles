
-- Standard awesome library
local gears = require("gears")
local awful = require("awful")
-- Theme handling library
local beautiful = require("beautiful")
-- Widget and layout library
local wibox = require("wibox")
-- Notification library
local naughty = require("naughty")
local menubar = require("menubar")
local hotkeys_popup = require("awful.hotkeys_popup")
require("awful.hotkeys_popup.keys")

-- Modules
local defaults = require('config.vars.defaults')



-- {{{ Menu
-- Create a launcher widget and a main menu
menus = {}

menus.myawesomemenu = {
    { " HotKeys", function() hotkeys_popup.show_help(nil, awful.screen.focused()) end },
    { " Man Page", defaults.terminal .. ' -e man awesome' },
    { " Edit config", defaults.editor .. ' ' .. awesome.conffile .. '/../' },
    { " Reload", awesome.restart },
}

menus.openapps = {
    { " Terminal", defaults.terminal   },
    { " Browser", "brave" },
    { " Music Player", "spotify" },
    { " Files", "thunar" }
}

menus.system = {
    { " Close Session", function() awesome.quit() end },
    { " Restart", "reboot" },
    { " Shutdown", "shutdown now"}
}

menus.mymainmenu = awful.menu({
    items = {
        { "W W manager", menus.myawesomemenu },
        { " Open Apps", menus.openapps },
        { " System", menus.system }
    }
})

menus.mylauncher = awful.widget.launcher({
    image = beautiful.awesome_icon,
    menu = menus.mymainmenu
})

-- Menubar configuration
menubar.utils.terminal = defaults.terminal
-- Set the terminal for applications that require it
-- }}}

return menus