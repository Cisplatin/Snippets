/*
  Diophantine Reciprocals I
  Problem 108
*/

#include <iostream>

const uint64_t DISTINCT = 1000;

// Returns the number of solutions for 1/x + 1/y = 1/n
// @param [n] The number to find the solution for
// @return The number of solutions
uint64_t diophantine(uint64_t n) {
  uint64_t total_solutions = 0;
  for(uint64_t x = n + 1; x <= 2 * n; x++) total_solutions += ((x * n) % (x - n) == 0);
  return total_solutions;
}

int main(int argc, char *argv[]) {
  // Go through each possible number until we find a solution greater than DISTINCT
  uint64_t current = 0;
  while(diophantine(++current) < DISTINCT);

  // Print the value that exceeded DISTINCT
  std::cout << current << std::endl;
  return 0;
}
