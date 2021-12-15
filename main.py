from vpython import *
from rate import *

tv = False
def T_f():
    global tv
    tv = not tv
    return

# Buttons
button(text='Faster', bind=inc_rate)
button(text='Slower', bind=dec_rate)
button(text='test', bind=T_f)

test_s = sphere(pos=vector(2,2,0), make_trail = True, trail_type = 'points', interval = 5, retain = 15) # Test sphere
test_s.p = vector(0,0,5) # Sphere angular momentum

dt = 0.01
# Main run loop
while True:
    rate(rate_value)
    F = - 50 * test_s.pos.hat / mag2(test_s.pos)
    test_s.p += F*dt
    test_s.pos = test_s.pos + test_s.p*dt

    if tv:
        rate_value = 200
    else:
        rate_value = 500