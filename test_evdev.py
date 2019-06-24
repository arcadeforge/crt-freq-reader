from evdev import UInput, ecodes as e

ui = UInput ()
ui.write(e.EV_KEY, e.KEY_A, 1)
ui.write(e.EV_KEY, e.KEY_A, 0)
ui.syn()
ui.close()

