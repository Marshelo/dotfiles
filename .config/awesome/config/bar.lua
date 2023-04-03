-- Modules
local keys = require('config.keys')
local defaults = require('config.vars.defaults')
local taglist = require('config.vars.taglist')
local layoutlist = require('config.vars.layoutlist')
local menus = require('config.menus')

-- Standard awesome library
local gears = require("gears")
local awful = require("awful")
local beautiful = require("beautiful")

-- Widget and layout library
local wibox = require("wibox")

local bar = {}

mylauncher = awful.widget.launcher({ image = '/home/shelo/.config/awesome/src/img/wm_menu2.png',
                                     menu = menus.mymainmenu })

-- {{{ Wibar
-- Keyboard map indicator and switcher
bar.mykeyboardlayout = awful.widget.keyboardlayout()
-- Create a textclock widget
bar.mytextclock = wibox.widget.textclock()

-- Create a wibox for each screen and add it
bar.taglist_buttons = gears.table.join(
    awful.button({ }, 1, function(t) t:view_only() end),
    awful.button({ modkey }, 1, function(t)
        if client.focus then
            client.focus:move_to_tag(t)
        end
    end),
    awful.button({ }, 3, awful.tag.viewtoggle),
    awful.button({ modkey }, 3, function(t)
        if client.focus then
            client.focus:toggle_tag(t)
        end
    end),
    awful.button({ }, 4, function(t) awful.tag.viewnext(t.screen) end),
    awful.button({ }, 5, function(t) awful.tag.viewprev(t.screen) end)
)

bar.tasklist_buttons = gears.table.join(
    awful.button({ }, 1, function (c)
        if c == client.focus then
            c.minimized = true
        else
            c:emit_signal(
                "request::activate",
                "tasklist",
                {raise = true}
            )
        end
    end),
    awful.button({ }, 3, function()
        awful.menu.client_list({ theme = { width = 250 } })
    end),
    awful.button({ }, 4, function ()
        awful.client.focus.byidx(1)
    end),
    awful.button({ }, 5, function ()
        awful.client.focus.byidx(-1)
    end))

-- local function set_wallpaper(s)
--     -- Wallpaper
--     if beautiful.wallpaper then
--         local wallpaper = beautiful.wallpaper
--         -- If wallpaper is a function, call it with the screen
--         if type(wallpaper) == "function" then
--             wallpaper = wallpaper(s)
--         end
--         gears.wallpaper.maximized(wallpaper, s, true)
--     end
-- end

-- Re-set wallpaper when a screen's geometry changes (e.g. different resolution)
-- screen.connect_signal("property::geometry", set_wallpaper)
awful.screen.connect_for_each_screen(function(s) -- s = screen
    -- local tags = {}
    -- Set tags according to the files in settings folder
    -- See: modules/settings/taglist and "/"/layoutlist
    -- for i = 1, #taglist.settings do
    --     table.insert(tags, awful.tag.add(taglist.settings[i].name, {
    --         screen = s,
    --         layout = taglist.settings[i].layout,
    --     }))
    -- end
    -- awful.tag.setproperty(taglist.settings[1].name, "layout", layoutlist[3])
    taglist.setTags(s)
    -- awful.tag.add('lol', { screen = s, }) -- En caso de emergencias
    -- Create a promptbox for each screen
    s.mypromptbox = awful.widget.prompt()
    -- Create an imagebox widget which will contain an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(gears.table.join(
        awful.button({ }, 1, function () awful.layout.inc( 1) end),
        awful.button({ }, 3, function () awful.layout.inc(-1) end),
        awful.button({ }, 4, function () awful.layout.inc( 1) end),
        awful.button({ }, 5, function () awful.layout.inc(-1) end)))
    -- Create a taglist widget
    -- awful.taglist({screen = s, filter  = awful.widget.taglist.filter.all, buttons = bar.taglist_buttons})
    -- s.mytaglist = awful.widget.taglist({
    --     screen = s,
    --     awful.widget.taglist.filter.all,
    --     bar.taglist_buttons,
    -- })

    -- s.container = ################################


    s.mytaglist = awful.widget.taglist {
        screen  = s,
        filter  = awful.widget.taglist.filter.all,
        buttons = bar.taglist_buttons,
        -- layout   = {
        --     layout  = wibox.layout.fixed.horizontal
        -- },
        widget_template = {
            {
                {
                    {
                        id     = 'text_role',
                        widget = wibox.widget.textbox,
                    },
                    layout = wibox.layout.fixed.horizontal,
                },
                left  = -2,
                right = -2,
                widget = wibox.container.margin
            },
            id     = 'background_role',
            widget = wibox.container.background,
            -- Add support for hover colors and an index label
            create_callback = function(self, c3, index, objects) --luacheck: no unused args
                self:connect_signal('mouse::enter', function() -- When the mouse is over the tag
                    if self.fg ~= '#ff0000' then
                        self.backup     = self.fg
                        self.has_backup = true
                    end
                    self.fg = '#ff0000'
                end)
                self:connect_signal('mouse::leave', function() -- When the mouse leave the tag
                    if self.has_backup then self.fg = self.backup end
                end)
            end,
            update_callback = function(self, c3, index, objects) --luacheck: no unused args
            end,
        },
    }

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist {
        screen  = s,
        filter  = awful.widget.tasklist.filter.currenttags,
        buttons = bar.tasklist_buttons
    }

    -- Create the wibox
    s.mywibox = awful.wibar({ position = "bottom", screen = s })

    -- Add widgets to the wibox
    s.mywibox:setup {
        {
            layout = wibox.layout.align.horizontal,
            { -- Left widgets
                layout = wibox.layout.fixed.horizontal,
                mylauncher,
                s.mytaglist,
                s.container,
                s.mypromptbox,
            },
            s.mytasklist, -- Middle widget
            { -- Right widgets
                layout = wibox.layout.fixed.horizontal,
                bar.mykeyboardlayout,
                wibox.widget.systray(),
                bar.mytextclock,
                s.mylayoutbox,
            },
        },
        bottom = 4, -- don't forget to increase wibar height
        color = '',
        widget = wibox.container.margin
    }
end)
-- }}}


return bar
