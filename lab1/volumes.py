#!/usr/bin/env python


def cylinder_volume (radius,height):
    import math
    if radius <0:
        return None

    if height <0:
        return None

    return math.pi*(radius**2)*height

def torus_volume (major_R, minor_R):
    import math
    if major_R <0:
        return None
    if minor_R <0:
        return None

    return math.pi*minor_R**2*2*math.pi*major_R 


if __name__ == '__main__': 

    radius_test = 2 #inches
    height_test = 4

    cyl_volume = cylinder_volume(radius_test, height_test)

    print "Cylinder volume is", cyl_volume, "in^3"

    torus_minor_R = 3 #inches
    torus_major_R = 4

    tor_volume = torus_volume(torus_major_R, torus_minor_R)

    print "Torus volume is", tor_volume, "in^3"
