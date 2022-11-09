import os
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#---------------#
#   COLORS      #
#---------------#

# 0 - black
# 1 - red
# 2 - green
# 3 - yellow
# 4 - blue
# 5 - magenta
# 6 - cyan
# 7 - white

colors = []
cache='/home/fjp/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

#---------------#
#   SUPER KEY   #
#---------------#
mod = "mod4"

#---------------#
#   KEYBINDINGS #
#---------------#

keys = [

    #---    Switch between windows  ---#
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),

    #---    Move windows    ---#
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    #---    Resize windows  ---#
    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),

    #---    Get windows original size   ---#
    Key([mod], "n", lazy.layout.normalize()),

    #---    Get screenshot  ---#
    Key([mod], "x", lazy.spawn("bash /home/fjp/.config/rofi/applets/bin/screenshot.sh")),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),

    #---    Browser     ---#
    Key([mod], "b", lazy.spawn("firefox")),

    #---    Terminal    ---#
    Key([mod], "Return", lazy.spawn("kitty")),

    #---    Launcher    ---#
    Key([mod], "space", lazy.spawn("rofi -show run")),

    #---    Toogle layout   ---#
    Key([mod], "Tab", lazy.screen.next_group()),

    #---    Toggle Group    ---#
    # Key([mod], "Tab", lazy.group.next_window()),

    #---    Kill window     ---#
    Key([mod], "w", lazy.window.kill()),

    #---    Reload Qtile    ---#
    Key([mod, "shift"], "r", lazy.reload_config()),

    #---    Exit Qtile      ---#
    Key([mod, "shift"], "q", lazy.shutdown()),

    #---    Brightness up   ---#
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),

    #---    Brightness down ---#
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

    #---    Lock screen ---#
 #   Key([], "F1", lazy.spawn("betterlockscreen --lock blur"))
]

#---------------#
#   WORKSPACES  #
#---------------#

groups = [Group("I"),
          Group("II"),
          Group("III"),
          Group("IV"),
          Group("V")
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

#---------------------------#
#   WINDOW STYLE IN LAYOUTS #
#---------------------------#

layouts = [
    # layout.MonadTall(border_focus=colors[2], border_normal=colors[0], border_width=1, margin=8),
    layout.Bsp(border_focus=colors[7], border_normal=colors[0], border_width=1, margin=8),
    layout.Max(),
    # layout.MonadWide(border_focus=colors[2], border_normal=colors[0], border_width=1, margin=8),
    # layout.RatioTile(border_focus=colors[2], border_normal=colors[0], border_width=1, margin=8),
    # layout.Matrix(),
]

#-----#
# BAR #
#-----#

widget_defaults = dict(
    font="FiraCodeMono Nerd Font",
    fontsize=18,
    padding=6,
)
extension_defaults = widget_defaults.copy()

delimiter_text=' 卑'
delimiter_size=60
delimiter_padding=-17

screens = [
    Screen(
        wallpaper='~/.config/qtile/wallpaper.png',
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.TextBox(
                    background=colors[0],
                    foreground=colors[7],
                    text=''
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active=colors[7],
                    rounded=False,
                    block_highlight_text_color=colors[2],
                    highlight_method="text",
                    borderwidth=0,
                    disable_drag=True,
                    urgent_text=colors[1]
                ),
                widget.WindowName(
                    foreground=colors[7],
                    markup=True,
                    max_chars=63
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[0],
                    foreground=colors[3],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.Net(
                    interface="wlp1s0",
                    format="{down}   {up}",
                    background=colors[3],
                    foreground=colors[0],
                    update_interval=1.0,
                    use_bits=True,
                    prefix='M'
                ),
                widget.Wlan(
                    background=colors[3],
                    foreground=colors[0],
                    format='{essid} {percent:2.0%}',
                    interface='wlp1s0',
                    update_interval=1.0
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[3],
                    foreground=colors[2],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.TextBox(
                text=' ',
                    background=colors[2],
                    foreground=colors[0],
                    padding=7
                ),
                widget.CurrentLayout(
                    background=colors[2],
                    foreground=colors[0],
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[2],
                    foreground=colors[6],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.ThermalZone(
                    format="  {temp}°C",
                    fgcolor_normal=colors[0],
                    background=colors[6],
                    zone="/sys/class/thermal/thermal_zone0/temp"
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[6],
                    foreground=colors[4],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.Memory(
                    format=" 𧻓{MemUsed: .0f}{mm}",
                    background=colors[4],
                    foreground=colors[0],
                    interval=1.0
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[4],
                    foreground=colors[5],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.Battery(
                    background=colors[5],
                    foreground=colors[0],
                    charge_char='  ',
                    discharge_char='  ',
                    format='{char} {percent:2.0%}',
                    low_foreground=colors[1],
                    low_percentage=0.2
                ),
                widget.TextBox(
                    text=delimiter_text,
                    background=colors[5],
                    foreground=colors[1],
                    padding=delimiter_padding,
                    fontsize=delimiter_size
                ),
                widget.Clock(
                    background=colors[1],
                    foreground=colors[0],
                    format="%l:%M %p - %a - %b %d %y",
                    update_interval=60.0
                ),
                
            ],
            25,
            background=colors[0],
        ),
    ),
]

#-----------------------#
#   FLOATING WINDOWS    #
#-----------------------#



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

#---------------#
#   AUTOSTART   #
#---------------#


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
