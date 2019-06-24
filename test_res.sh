#hdmi_timings="320 1 2 26 43 240 1 3 7 12 0 0 0 60 0 6400000 1"


hdmi_timings="450 1 50 30 90 270 1 1 1 30 0 0 0 50 0 9600000 1"

/opt/vc/bin/vcgencmd hdmi_timings $hdmi_timings

sleep 0.3
tvservice -e "DMT 87"
sleep 0.3

fbset -g 450 270 450 270 24 > /dev/null
#fbset -g 320 240 320 240 24 > /dev/null
#fbset -depth 8 && fbset -depth 24 -xres 320 -yres 240 > /dev/null
#fbset -depth 8 && fbset -depth 24 

#fbset -depth 8 && fbset -depth 16
#fbset -g 450 270 450 270 24 > /dev/null
# fb not put to screen
#echo "post res executed"

python3 read_freq.py
