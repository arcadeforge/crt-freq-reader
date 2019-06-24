sleep 1
hdmi_timings="450 1 50 30 90 270 1 1 1 30 0 0 0 50 0 9600000 1"
/opt/vc/bin/vcgencmd hdmi_timings $hdmi_timings 

sleep 0.3

tvservice -e "DMT 87"

sleep 0.3

#fbset -g 450 270 450 270 24

fbset -depth 8 && fbset -depth 24 -xres 450 -yres 270 > /dev/null
#fbset -depth 8 && fbset -depth 24 > /dev/null


#fbset -depth 8 && fbset -depth 16
#fbset -g 450 270 450 270 24 > /dev/null
# fb not put to screen
#echo "post res executed"
