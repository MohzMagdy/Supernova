from vpython import button

dt = 0
running = False
prev_dt = 0.005

# Gets the value of dt to avoid errors in other files
def get_dt():
    global dt
    return dt

# Identifies weather program is running or paused
def get_running():
    global running
    return running

# Pauses the simulation if unpaused, and unpauses if paused
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

# Increases the value of dt, making simulation faster
def inc_rate():
    global dt
    dt += 0.0025

# Decreases the value of dt, making simulation slower
def dec_rate():
    global dt
    dt -= 0.0025