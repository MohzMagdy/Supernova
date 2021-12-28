# Initial rate
global rate_value 
rate_value = 200

# Increase rate
def inc_rate():
    global rate_value
    rate_value = 5000
    return

# Decrease rate
def dec_rate():
    global rate_value
    rate_value -= 2000
    return
