import numpy as np
import matplotlib.pyplot as plt

#Number of points to connect
npoints=9

#Number of times to iterate
niters=10

#Randomness of the angles to the initial points
jitter=1.0

#Function to find intersection of two lines
def line_intersection(p1, p2, p3, p4):
    """
    Find the intersection of two lines defined by points (p1, p2) and (p3, p4).
    Returns the intersection point as a tuple (x, y), or None if no intersection.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    # Line equations: (x, y) = p1 + t1 * (p2 - p1), (x, y) = p3 + t2 * (p4 - p3)
    # Solving for t1 and t2
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None  # Lines are parallel or coincident
    
    t1 = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    t2 = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denominator

    # Intersection point
    x = x1 + t1 * (x2 - x1)
    y = y1 + t1 * (y2 - y1)

    return (x, y)

#Create an array to hold the points and initialise it with sorted random numbers.
points = np.empty((npoints,2))
points[:,0] = [2*np.pi*i*(1+np.random.rand()*jitter/npoints)/npoints for i in range(0,npoints)]

#Create an array to hold the intersections of the lines
intersects = np.empty((npoints,2))

points[:,1] = np.cos(points[:,0])
points[:,0] = np.sin(points[:,0])

plt.figure(figsize=(6, 6))
for j in range(niters):
    for i in range(npoints):
        plt.plot([points[i][0], points[(i+2)%npoints][0]],[points[i][1], points[(i+2)%npoints][1]],color="green")
        intersects[i] = line_intersection(points[i], points[(i+2)%npoints], points[(i+1)%npoints], points[(i+3)%npoints])
        
    for i in range(npoints):
        plt.plot([intersects[i%npoints][0], intersects[(i+2)%npoints][0]],[intersects[i%npoints][1], intersects[(i+2)%npoints][1]],color="red")

    points[:]=intersects
