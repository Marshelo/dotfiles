local awful = require("awful")

local layoutlist = require('config.vars.layoutlist')

local taglist = {}

-- tags.keys = { '1', 'q', '2', 'w', '3', 'e', '4' }
-- This config is aplied to all screens
-- Note: the "key" variable is used to define the key
-- bindings associated with his tag
taglist.settings = {
    { name = '▀', key = '1', layout = layoutlist[1] },
    { name = '▃', key = 'q', layout = layoutlist[1] },
    { name = '▀', key = '2', layout = layoutlist[1] },
    { name = '▃', key = 'w', layout = layoutlist[1] },
    { name = '▀', key = '3', layout = layoutlist[1] },
    { name = '▃', key = 'e', layout = layoutlist[1] },
    { name = '▀', key = '4', layout = layoutlist[1] },
    { name = ' ▀', key = '5', layout = layoutlist[1] },
    -- { name = "other",   layout = layoutlist[1], setslave = true }, -- an example
}
taglist.instances = {}
taglist.setTags = function(s)
    awful.tag({ taglist.settings[1].name }, s, taglist.settings[1].layout)
    for i = 2, #taglist.settings do
        table.insert(taglist.instances, awful.tag.add(taglist.settings[i].name, {
            screen = s,
            layout = taglist.settings[i].layout,
        }))
    end
end
return taglist
