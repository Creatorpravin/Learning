#mousepad&

xdotool search --onlyvisible --class 'mousepad' windowactivate

sleep 2
xdotool type "Hello it do automation"
xdotool key KP_Enter
xdotool type "The second line"

sleep 2
xdotool key 'ctrl+q'
sleep 1
xdoteel key Left
sleep 1
xdotool key Left
sleep 1
xdotool key KP_Enter