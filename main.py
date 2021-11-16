#!/usr/bin/env python3
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ANGLE", help="The angle at which the projectale was fired", type=float)
parser.add_argument("SPEED", help="The speed at which the projectale was fired", type=float)
parser.add_argument("-g", help="Gravitational accelration spped in. Default is 9.8067 m/s^2", default=9.8067, type=float)
parser.add_argument("-y", help="The starting height of the projectale in meters. Default is 0",default=0, type=float)
args = parser.parse_args()

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
    x,t = projectleMotion(args.ANGLE, args.SPEED, args.g, args.y) 
    print(f'Traveled distance: {round(x,2)}m\nTime of traveled distance: {round(t,2)}s')