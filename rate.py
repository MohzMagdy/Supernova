start = True
Dec_Rate = False
Inc_Rate = False
def start(b):
    #while rate() == 1:
    global start, Inc_Rate, Dec_Rate
    start = not start
    Dec_Rate = False
    Inc_Rate = False
    return start, Inc_Rate, Dec_Rate
#Start = Start and Start
def Inc_Rate(I):
    #while rate() == 500 or rate()==1:
    global start, Inc_Rate, Dec_Rate
    Inc_Rate = not Inc_Rate
    start = False
    Dec_Rate = False
    return start, Inc_Rate, Dec_Rate
def Dec_Rate():
    #while rate() == 1000 or rate()== 500:
    global start, Inc_Rate, Dec_Rate
    Dec_Rate = not Dec_Rate
    start = False
    Inc_Rate = False
    return start, Inc_Rate, Dec_Rate