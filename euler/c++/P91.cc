/*
  Right Triangles with Integer Co-ordinates
  Problem 91
*/

#include <iostream>

const int32_t MAX_DIMENSION = 50;

int main(int argc, char *argv[]) {
  // We first add all the triangles that have a point on either the y-axis or x-axis. For each
  // of each points, we know there are MAX_DIMENSION triangles that can be made.
  int32_t triangles = 2 * MAX_DIMENSION * MAX_DIMENSION;

  // Fix the origin and one other point, A. Connect these points with a line OA. Then we can find
  // a point B such that OAB is a right triangle by selecting a point on the line that intersects
  // A and is perpendicular to OA. We do this for each possible A that is not on the axes.
  // Note that no double-counting is made because A is the point with the right angle.
  for(int32_t a = 1; a <= MAX_DIMENSION; a++) {
    for(int32_t b = a; b <= MAX_DIMENSION; b++) {

      // The line OA has a slope of A.y / A.x, and has an intercept of 0. So the line can be
      // described as y = xA.y / A.x. The perpendicular line would then have a slope of -A.x / A.y.
      // We want to find the particular line that intersects A, so we can have
      // A.y = -A.x^2 / A.y + b, or that b = (A.y^2 + A.x^2) / A.y. Thus the equation (where we
      // set A.x := a and A.y := b) is y = (b^2 + a^2 - xa) / b. So we just need solutions (x, y)
      // to this equation where x and y are integers in our bounds.
      int32_t max_y = a * a + b * b, limit = std::max(max_y - a * MAX_DIMENSION, 0);;
      while(max_y >= limit) {
        if(max_y % b == 0 && max_y / b <= MAX_DIMENSION) triangles += 1 + (a != b);
        max_y -= a;
      }
    }
  }

  // Print out the final answer
  std::cout << triangles << std::endl;
  return 0;
}
