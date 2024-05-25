#!/bin/bash

xdotool search --onlyvisible --class "mousepad" windowactivate

window_id = "xdotool getactivewindow"

xdotool mousemove 10 10
sleep 1
xdotool click 1
sleep 1
xdotool mousemove 10 10