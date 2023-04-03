local awful = require("awful")


modes = {}

function Set (list)
    local set = {}
    for _, l in ipairs(list) do set[l] = true end
    return set
end


-- Short cuts mode --
-- (mode with easy access to some functions)
-- (keybinding configured in keys.lua file, probably with super+d)

-- function keysCombinations(key)
--     keys = Set { 'q' } -- { 'q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c' }
--     if keys[key] then
--         naughty.notify({title = '¡Potoco!', text = 'lol'})
--     else
--         keygrabber.stop()
--     end
-- end

-- function modes.easyshortcuts()
--     -- mymainmenu:show()
--     if not keygrabber.isrunning() then
--         awful.keygrabber.run(function(mod, key, event)
--             if event == "press" then keysCombinations(key) end
--         end)
--     end
-- end

return modes