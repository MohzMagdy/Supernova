from vpython import button

dt = 0
running = False
prev_dt = 0.005

def get_dt():
    global dt
    return dt

def pause():
    global running, pause_button, dt, prev_dt
    if running:
        pause_button.text = 'Unpause'
        prev_dt = dt
        dt = 0
    else:
        pause_button.text = 'Pause'
        dt = prev_dt
    running = not running
pause_button = button(bind=pause, text='Start')

def inc_rate():
    global dt
    dt += 0.0025

def dec_rate():
    global dt
    dt -= 0.0025