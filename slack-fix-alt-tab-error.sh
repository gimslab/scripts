#!/bin/bash

# README
# http://wiki.gimslab.com/moniwiki/wiki.php/slack-alt-tab-error

# Enable developer tools within slack (right-click -> inspect)
export SLACK_DEVELOPER_MENU=true

/usr/bin/slack &

# Old slack icon, which I'm using because I'm used to it
#ICON=/usr/share/icons/slack.png
# New slack icon
ICON=/usr/lib/slack/resources/app.asar.unpacked/src/static/slack.png

# Lame way to give slack enough time to launch before attempting to modify it
sleep 10

# Find slack window(s) by name.  You need to handle multiple windows here to actually get multiple workspaces working w/icons
WINDOWS=(`wmctrl -l | grep "Slack - " | cut -f1 -d' ' | xargs`)
for slack_window in ${WINDOWS[@]}; do
    # Use "xseticon", a compiled C binary, to change the icon of a running program
    $HOME/xseticon -id ${slack_window} /usr/share/icons/slack.png

    # Use "xprop" to set the window state, so that alt+tab works again
    xprop -f _NET_WM_WINDOW_TYPE 32a -set _NET_WM_WINDOW_TYPE _NET_WM_WINDOW_TYPE_NORMAL -id ${slack_window}
done

