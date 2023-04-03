local awful = require("awful")
local gears = require('gears')
local naughty = require("naughty")

local menus = require('config.menus')

shortcut = {}

function Set (list)
    local set = {}
    for _, l in ipairs(list) do set[l] = true end
    return set
end

shortcut.mode = function ()
        awful.keygrabber.run(awful.keygrabber {
            start_callback = function() --[[do something]]  end,
            stop_callback  = function() --[[do something]] end,
            -- export_keybindings = true,

            stop_event = 'release',
            stop_key = {'Escape', 'Super_L', 'Super_R', 'm'},
            allowed_keys   = {'d', 'g'},

            keybindings = {
                {{ modkey } , "d" , function()
                    menus.mymainmenu:show()
                end},
                {{ modkey } , "g" , function()
                    naughty.notify({title = '¡Potoco!', text = 'lol'})
                    keygrabber:stop()
                end},
            }
        })
    end

return shortcut