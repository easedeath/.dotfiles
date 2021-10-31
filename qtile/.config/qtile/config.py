# -*- coding: utf-8 -*
import os
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
import psutil

def get_battery_status():
    if psutil.sensors_battery().power_plugged:
        return '  '
    else:
        return '  '

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

mod = "mod4"  
alt = "mod1"
ctrl = "control"
myTerm = "alacritty"  
home = os.path.expanduser('~')
scripts = home + "/.config/qtile/scripts/"
myConfig = home + "/.config/qtile/config.py"

keys = [
    # Some basic scripts
    Key(
        [ctrl, alt],
        "l",
        lazy.spawn(f"sh {scripts}/blur-lock.sh"),
        desc="launches i3-blur lock",
    ),
    Key(
      [mod],
      "b",
      lazy.hide_show_bar("bottom"),
    ),
    #LAUNCHING APPS with Ctrl + Alt + Key
    Key(
        [ctrl, alt],
        "p",
        lazy.spawn("planner"),
        desc=" Launches Planner",
    ),

    Key(
        [],
        "Print",
        lazy.spawn("gnome-screenshot -i"),
        desc="Screen_Shot",
    ),
    
    Key(
        [ctrl, alt],
        "b",
        lazy.spawn("firefox"),
        desc="Launches Firefox Browser",
    ),
    Key(
        [ctrl, alt],
        "e",
        lazy.spawn("evince"),
        desc="Launces Evince PDF Reader",
    ),
    Key([mod],
        "Return",
        lazy.spawn(myTerm),
        desc="Launches My Terminal with fish shell",
    ),

   # The essentials
    Key(
        [mod],
        "x",
        lazy.spawn(
            f"bash {home}/.config/rofi/applets/applets/powermenu.sh"
        ),
        desc="Shows rofi power-menu",
    ),

    Key(
        [mod],
        "z",
        lazy.spawn(
            f"bash {home}/.config/rofi/applets/applets/battery.sh"
        ),
        desc="Shows rofi power-menu",
    ),

    Key(
        [mod],
        "t",
        lazy.spawn(
            f"bash {home}/.config/rofi/applets/applets/time.sh"
        ),
        desc="Shows rofi power-menu",
    ),


    Key(
        [mod],
        "v",
        lazy.spawn(
            f"bash {home}/.config/rofi/applets/applets/volume.sh"
        ),
        desc="Shows rofi power-menu",
    ),

    
    Key(
        [mod, "shift"],
        "Up",
        lazy.spawn("amixer -D pulse sset Master 2%+"),
        desc="Granuler control over volume",
        ),

    Key(
        [mod, "shift"],
        "Down",
        lazy.spawn("amixer -D pulse sset Master 2%-"),
        desc="Granular control over volume",
    ),
    Key(
        [mod],
        "Up",
        lazy.spawn("amixer -D pulse sset Master 5%+"),
        desc="Increase Volume (pulse so that it automatically recognizes inserted devices)",
    ),
    Key(
        [mod],
        "Down",
        lazy.spawn("amixer -D pulse sset Master 5%-"),
        desc="Decrease Volume (pulse so that it automatically recognizes inserted devices)",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn(f"bash {home}/.config/rofi/launchers/text/launcher.sh"),
        desc="Run Launcher",
    ),
    
    #BASIC UTILITIES
    Key(
        [mod],
        "Tab",
        lazy.next_layout(),
        desc="Toggle through different layouts",
    ),
    Key(
        [mod],
        "q",
        lazy.window.kill(),
        desc="Kill/Quit active window "
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.restart(),
        desc="Restart Qtile without disturbing any other opened windows"
    ),
    Key(
        [mod, "shift"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile     ;)"
    ),
    
    # Window controls
    Key(
        [mod],
        "Right",
        lazy.screen.next_group(),
        desc="Move to next Group"
    ),
    Key(
        [mod],
        "Left",
        lazy.screen.prev_group(),
        desc="Move to previous Group"
    ),
    Key(
        [mod],
        "k",
        lazy.layout.down(),
        desc="Move focus down in current stack pane"
    ),
    Key(
        [mod],
        "j",
        lazy.layout.up(),
        desc="Move focus up in current stack pane"
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.normalize(),
        desc="normalize window size ratios"
        ),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="toggle floating"
    ),
    Key(
        [mod, "shift"],
        "m",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen"
    ),
    # Stack controls
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "control"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

workspaces = [
    {
        "name": "www",
        "key": "1",
        "matches": [Match(wm_class="firefox")]
    },
    {
        "name": "vim",
        "key": "2",
        "matches": [Match(wm_class="code")],
    },
    {
        "name": "sys",
        "key": "3",
        "matches": []
    },
    {
        "name": "doc",
        "key": "4",
        "matches": [Match(wm_class="evince")],
    },
    {
        "name": "chat",
        "key": "5",
        "matches": [Match(wm_class="discord"), Match(wm_class="telegram-desktop")],
    },
    {
       "name": "xyz",
       "key": "6",
        "matches": [],
    },

    {
       "name": "vid",
       "key": "7",
        "matches": [Match(wm_class="vlc")],
    },
]
groups = []

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout="Monadtall"))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )


layout_theme = {
    "border_width": 0,
    "margin": 0,
    "border_focus": "#88c0d0",
    "border_normal": "#1D2330",
}

layouts = [
    layout.MonadTall(**layout_theme),
    #layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

colors = [
    ["#2e3440", "#2e3440"],  # 0. background
    ["#d8dee9", "#d8dee9"],  # 1. foreground
    ["#3b4252", "#3b4252"],  # 2. background lighter
    ["#bf616a", "#bf616a"],  # 3. red
    ["#a3be8c", "#a3be8c"],  # 4. green
    ["#ebcb8b", "#ebcb8b"],  # 5. yellow
    ["#84A7C0", "#84A7C0"],  # 6. blue
    ["#b48ead", "#b48ead"],  # 7. magenta
    ["#88c0d0", "#88c0d0"],  # 8. cyan
    ["#e5e9f0", "#e5e9f0"],  # 9. white
    ["#4c566a", "#4c566a"],  # 10. grey
    ["#d08770", "#d08770"],  # 11. orange
    ["#8fbcbb", "#8fbcbb"],  # 12. super cyan
    ["#5e81ac", "#5e81ac"],  # 13. super blue
    ["#242831", "#242831"],  # 14. super dark background
]

widget_defaults = dict(font="SauceCodePro Nerd Font", fontsize=30, padding=2, background=colors[0])
extension_defaults = widget_defaults.copy()

group_box_settings = {
    "padding": 3,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[11],
    "highlight_method": "block",
    "this_current_screen_border": colors[0],
    "this_screen_border": colors[2],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[0],
    "urgent_border": colors[3],
}

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    font="SauceCodePro Nerd Font",
                    fontsize=17,
                    visible_groups=["www", "vim", "sys", "doc", "chat","xyz","vid"],
                    **group_box_settings,
                ),
                
                widget.Spacer(),
                widget.Systray(
                    icon_size=18, padding=5, background=colors[0], foreground=colors[10]
                ),
                widget.Spacer(length=20, background = colors[0]),
            ],
            30,
        ),
        top=bar.Gap(0),
        left=bar.Gap(0),
        right=bar.Gap(0),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        Match(wm_type="utility"),
        # Match(wm_type='notification'),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="file_progress"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="feh"),
        Match(func=lambda c: c.has_fixed_size()),
    ]
)


auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
    subprocess.call(["feh","--bg-fill",f"{home}/.config/qtile/wallpaper.png"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
