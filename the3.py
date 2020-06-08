#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() OR ANYTHING IN draw.py HERE AGAIN

from evaluator import *

mainlist = get_data()
List = get_data()
dt = float(mainlist[1])
g = float(mainlist[0])
variab = 0
def new_move():
    global variab
    global dt
    global g
    global List
    global mainlist
    if List == mainlist and variab==0 : ## (if the call is the fist one) since L hasnt changed yet, it will be same as the default get_data.
        D = displacement_list(List)  ######returns [[dx,dy] [dx1, dy1]....]
        i = 2
        variab = 1
        while i < len(mainlist):
            List[i][1] += D[i-2][0]  ##### L = get_data() = [g,dt,[m,x,y,vx,vy],[m,,,]......]
            List[i][2] += D[i-2][1]  ##### they increase particles' x and y coordinates by delta x.
            i +=1
        return D  #### it should always return delta x. ( that is what we are asked ).
    else: ### if call is not the first one. the L will have been changed already. note that mainlist remains the same !
        A = acceleration_list()  ### A = [[ax,ay][ax2,ay2].....[axn,ayn]]
                                     ### List = [g,dt,[m,x,y,vx,vy][......]......]
        i=2
        j=0
        while i<len(List):     ### velocities are updated by a*t
            List[i][3] += A[j][0]*dt
            List[i][4] += A[j][1]*dt
            i+=1
            j+=1
        D = displacement_list(List)
        return D


def acceleration_list():    ####### returns [[ax,ay][ax1,ay1].....]
    import math
    global g
    global List
    particles = List[2:]
    Acclist = []
    i = 0
    k = len(particles)
    accsumx = 0
    accsumy = 0
    while i < k:
        item = particles[0]
        j = 1
        while j < k:
            a = float(particles[j][1]) - float(item[1])
            b = float(particles[j][2]) - float(item[2])
            d = math.hypot(a, b)
            accsumx += (g * particles[j][0] * (particles[j][1] - item[1])) / d ** 3  ###acceleration calculation<
            accsumy += (g * particles[j][0] * (particles[j][2] - item[2])) / d ** 3
            j += 1
        Acclist.append([accsumx, accsumy])
        particles.append(particles[0])
        particles = particles[1:]
        i += 1
        accsumx = 0
        accsumy = 0
    return Acclist

def displacement_list(L):

    global dt
    particles = L[2:]
    dislist = []
    i = 0
    while i < len(particles):
        x = particles[i][1]
        y = particles[i][2]
        vx = particles[i][3]
        vy = particles[i][4]
        dx = vx * dt
        dy = vy * dt
        dislist.append([dx, dy])
        i += 1
    return dislist

