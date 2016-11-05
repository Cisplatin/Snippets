/*
  Square Remainders
  Problem 120
*/

#include <iostream>
#include <algorithm>

const uint32_t LOWER_LIMIT = 3;
const uint32_t UPPER_LIMIT = 1000;

int main(int argc, char *argv[]) {
  uint32_t total_sum = 0;
  for(uint32_t i = LOWER_LIMIT; i <= UPPER_LIMIT; i++) {
    // For each power of n, if n is even the result is 2, and if n is odd the result is 2ni.
    uint32_t maximum = 0, base = 2 * i, modulos = i * i;
    for(uint32_t n = 1; n < i; n++) {
      maximum = std::max(maximum, (base * n) % modulos);
    }
    total_sum += maximum;
  }

  // Print out the final result
  std::cout << total_sum << std::endl;
  return 0;
}
