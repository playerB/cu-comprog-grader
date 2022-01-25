def distance1(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    dis = (dx**2 + dy**2)**0.5
    return dis

def distance2(p1, p2):
    dis = distance1(p1[0], p1[1], p2[0], p2[1])
    return dis

def distance3(c1, c2):
    overlap = False
    d3 = distance1(c1[0], c1[1], c2[0], c2[1])
    if d3 <= c1[2] + c2[2]:
        overlap = True
    return d3,overlap

def perimeter(points):
    peri = 0
    for i in range(len(points)):
        peri += distance2(points[i], points[(i+1)%len(points)])
    return peri

exec(input().strip())