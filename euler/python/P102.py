"""
Triangle Containment
Problem 102
"""

TRIANGLES_TXT = "P102.txt"
POINTS = 3
ORIGIN = (0, 0)


triangles = []

# Read the file as a set of tuples (i.e. each point)
with open(TRIANGLES_TXT, 'r') as f:
    for i in map(lambda x: map(int, x[:-1].split(",")), f.readlines()):
        triangles.append([(i[2 * j], i[2 * j + 1]) for j in xrange(POINTS)])

# For read-ability, the first index of 2-element tuples are refered to as x,
# and the second as y
x, y = 0, 1

# For each triangle, make sure the ORIGIN is on the same side of each line
# as the third point in question. We represent side as a boolean.
def side_of(a, b, c):
    if b[x] == c[x]:
        return a[x] > b[x]
    slope = (b[y] - c[y]) / float(b[x] - c[x])
    return a[y] > a[x] * slope + c[y] - slope * c[x]

# Returns true if the ORIGIN is contained by the triangle
def contained(a, b, c):
    return side_of(a, b, c) == side_of(ORIGIN, b, c) and \
           side_of(b, a, c) == side_of(ORIGIN, a, c) and \
           side_of(c, a, b) == side_of(ORIGIN, a, b)

print sum(contained(*i) for i in triangles)
