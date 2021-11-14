#!/usr/bin/env python3
import math



def projectleMotion(o: float, v: float, g: float = 9.8067, y: float = 0) -> tuple:
    """ Calculating ballistic curve based on:
        o - the angle at which the projectale was fired 
        v - the speed at which the projectale was fired
        g - gravitational accelration spped in m/s^2
        y - starting height of the projectale
        
        Returned data is a tuple in format = (y, d) where
        d - distance traveled by projectale 
        t - time at which projectale traveled d distance
    """
    # Calculating distance traveled by projectale
    if o == 45 and y == 0:
        d = (v**2)/g
    elif y == 0:
        d = ((v**2) * math.sin(2*o)) / g
    else:
        d = (v * math.cos(o))/g
        d *= (v * math.sin(o) + math.sqrt((v * math.sin(o))**2 + (2*g*y)))

    # Calculating time at which projectale traveled d distance
    if o == 45 and y == 0:
        t = (math.sqrt(2) * v)/g
    else:
        t = d / (v * math.cos(o))
    
    return (d, t)


if __name__ == '__main__':
    angle = 32
    speed = 50
    gravity = 10
    y = 200 # Starting height in meters
    # x-traveled distance in meters and t-time in seconds
    x,t = projectleMotion(angle, speed, gravity, y) 
    print(f'Traveled distance: {round(x,2)}m\nTime of traveled distance: {round(t,2)}s')