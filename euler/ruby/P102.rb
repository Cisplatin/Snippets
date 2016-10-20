"""
  Triangle Containment
  Problem 102
"""

TRIANGLES_TXT = "P102.txt"
DIMENSIONS = 2
ORIGIN = [0] * DIMENSIONS
DELTA = 0.000001

# We first format the file into arrays of triangles.
triangles = File.read(TRIANGLES_TXT).split("\n")
triangles.map!{ |n| n.split(",").map(&:to_i).each_slice(DIMENSIONS).to_a }

# Returns the area of the triangle defined by the three given points. We do this via Heron's formula
def triangle_area(*sides)
  lengths = (-1...DIMENSIONS)
            .map{ |i| Math.sqrt((0...DIMENSIONS)
            .map{ |j| (sides[i][j] - sides[i - 1][j]) ** 2 }.inject(:+)) }
  Math.sqrt(lengths.push(0).map{ |i| lengths.inject(:+) / Float(2) - i }.inject(:*))
end

# Checks the area of each triangle formed by two points and the origin, and the triangle itself.
# If the areas are equal, then the origin is bounded by the triangle. Because floats suck, we only
# get an approximate equality using DELTA.
puts triangles.select{ |i| (i.combination(DIMENSIONS).to_a.map{ |j| triangle_area(*j, ORIGIN) }
                             .inject(:+) - triangle_area(*i)).abs < DELTA }.count
