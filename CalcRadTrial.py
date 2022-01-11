from vpython import*


# def CalcRadiation(T):
    # y_max=T*0.002897755
    # print('maximum lamda',y_max)
curve=gcurve(color=color.black,label='Blackbody spectrum')
    # h=6.626*10**-34
    # c=3*10**8
    # # y=2*(10**-7)
    # k=1.38*(10**-23)
for y in arange(2,14,100):
        # while True:
            # try:
    B=(y**2)*9
                # B=(2*float(h)*(float(c)**2) / (float(y)**5)) / ( exp**( (float(h)*float(c))/(float(y)*float(k)*float(T)) ) -1 )
                # break
            # except:
                # print('invalid')
curve.plot(pos=(y,B))
        # return z


T=7000
# p=sphere(pos=vector(2,0,0),radius=0.2,color=color.blue)
# CalcRadiation(T) 