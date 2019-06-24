# compute vmax = freqh_h/ freq_v
# get hdmi_timings, then compute porches and compare to real vmax
# compute pclock 


import RPi.GPIO as GPIO
import time
import sys
import os

debug = False
#debug = True


RUN_TIME = 5.0
SAMPLE_TIME = 1.0

v_freq_m = 0
h_freq_m = 0

# hdmi-timings
x_res = 320
h_fp = 12
h_sync = 22
h_bp = 52
y_res = 240
v_fp = 5
v_sync = 7
v_bp = 11
freq = 60
pixel_clock = 6400000

# File interface
file = open ("hdmi_timing.txt", "r")
file_sav = open ("result.txt", "a") 


def main():

    global RUN_TIME
    global SAMPLE_TIME

    global v_freq_m
    global h_freq_m
    global v_max

    if len(sys.argv) > 1:
        RUN_TIME = int(sys.argv[1])    

    read_hdmi_timings (file)
    setResolution (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock)



    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(27, GPIO.RISING)
    GPIO.add_event_detect(22, GPIO.RISING)

    
    start = time.time()
    GPIO.add_event_callback(27, my_callback_v )
    GPIO.add_event_callback(22, my_callback_h )



    while (time.time() - start ) < RUN_TIME:
        time.sleep (SAMPLE_TIME)

    print ("stop")

    #GPIO.output(26, GPIO.HIGH)

    #GPIO.cleanup(26)
    v_freq_m = v_freq_m / RUN_TIME
    h_freq_m = h_freq_m / RUN_TIME

    save_hdmi_timings(file_sav)





def my_callback_v(self):
    global v_freq_m
    #print("detected" , v_freq_m)
    v_freq_m = v_freq_m + 1

def my_callback_h(self):
    global h_freq_m
    #print("detected" , ctr)
    h_freq_m = h_freq_m + 1


def read_hdmi_timings(file):

    global x_res
    global h_fp 
    global h_sync
    global h_bp
    global y_res
    global v_fp
    global v_sync
    global v_bp
    global freq
    global pixel_clock

    hdmi_timing = file.readline()
    hdmi_values = hdmi_timing.split()
    x_res = int(hdmi_values[0])
    h_fp = int(hdmi_values[2])
    h_sync = int(hdmi_values[3])
    h_bp = int(hdmi_values[4])
    y_res = int(hdmi_values[5])
    v_fp = int(hdmi_values[7])
    v_sync = int(hdmi_values[8])
    v_bp = int(hdmi_values[9])
    # should be float?
    freq = float(hdmi_values[13])
    pixel_clock = float(hdmi_values[15])
    file.close()


def save_hdmi_timings(file):

    v_max = h_freq_m / v_freq_m
    v_max_comp = y_res + v_fp + v_sync + v_bp
    h_max_comp = x_res + h_fp + h_sync + h_bp
    h_max = pixel_clock / v_freq_m / v_max

    pclk_m = round ((h_max * v_max * v_freq_m) ,0)
    pclk_c = round ((h_max_comp * v_max_comp * freq) ,0)

    file.write("%s 1 %s %s %s %s 1 %s %s %s 0 0 0 %s 0 %s 1\n" % (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock))
    file.write("Modeline \"%sx%s_%s\" %s %s %s %s %s %s %s %s %s -hsync -vsync\n" % (x_res, y_res, freq, pixel_clock /1000000, x_res, x_res+h_fp, x_res+h_fp+h_sync, x_res+h_fp+h_sync+h_bp, y_res, y_res+v_fp, y_res+v_fp+v_sync, y_res+v_fp+v_sync+v_bp))

    file.write("detected vertical freq : %s\n" % (v_freq_m))
    file.write("detected horizontal freq : %s\n" % (h_freq_m))
    file.write("real v_max : %s\n" % (round(v_max,0)))
    file.write("v_max computed : %s\n" % (round(v_max_comp,0)))
    file.write("real h_max : %s\n" % (round (h_max,0)))
    file.write("h_max computed : %s\n" % (round(h_max_comp,0)))

    file.write("v porches deviation : %s" % (round ((v_max_comp - v_max),0)))
    file.write("h porches deviation : %s" % (round ((h_max_comp - h_max),0)))

    file.write("measured pixel cloxk : %s" % (pclk_m))
    file.write("computed pixel cloxk : %s" % (pclk_c))

    file.write("=========================================================\n")
    file.close()

    print("%s 1 %s %s %s %s 1 %s %s %s 0 0 0 %s 0 %s 1\n" % (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock))
    print("detected vertical freq : " , v_freq_m)
    print("detected horizontal freq : " , h_freq_m)
    print("real v_max : " , round(v_max, 0))
    print("v_max computed : %s" % (round (v_max_comp, 0)))
    print("real h_max : %s" % (round (h_max, 0)))
    print("h_max computed : %s" % (round (h_max_comp, 0)))
    print("v porches deviation : %s" % (round ((v_max_comp - v_max),0)))
    print("h porches deviation : %s" % (round ((h_max_comp - h_max),0)))

    print("measured pixel cloxk : %s" % (pclk_m))
    print("computed pixel cloxk : %s" % (pclk_c))

def setResolution(x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock):

    #print("setResolution")
    if debug == True:
        pass
        #os.popen("sleep 0") 
        #print("vcgencmd hdmi_timings %s 1 %s %s %s %s 1 %s %s %s 0 0 0 %s 0 %s 1" % (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock))
        #print("tvservice -e \"DMT 87\"")
        #print("fbset -depth 8 && fbset -depth 24 -xres " + str(x_res) + " -yres " + str(y_res))
    else:
        #os.popen("/opt/vc/bin/vcgencmd hdmi_timings 320 1 12 22 52 240 1 5 7 11 0 0 0 60 0 6400000 1")

        os.popen("/opt/vc/bin/vcgencmd hdmi_timings %s 1 %s %s %s %s 1 %s %s %s 0 0 0 %s 0 %s 1" % (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock))
        print("vcgencmd hdmi_timings %s 1 %s %s %s %s 1 %s %s %s 0 0 0 %s 0 %s 1" % (x_res, h_fp, h_sync, h_bp, y_res, v_fp, v_sync, v_bp, freq, pixel_clock))

        os.popen("tvservice -e \"DMT 87\"")
        os.popen("sleep 0.3") 

        os.popen("fbset -depth 8 && fbset -depth 24")

        #os.popen("fbset -depth 8 && fbset -depth 16 -xres " + str(x_res) + " -yres " + str(y_res))

        #os.popen("fbset -g 320 240 320 240 24")
        #os.popen("fbset -depth 8 && fbset -depth 16 -xres " + str(x_res) + " -yres " + str(y_res))

        os.popen("sleep 0.3") 


        


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
