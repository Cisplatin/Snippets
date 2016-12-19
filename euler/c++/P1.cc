/*
  Multiples of 3 and 5
  Problem 1
*/

#include <iostream>

const uint64_t UPPER_LIMIT = 1000;

int main(int argc, char *argv[]) {
  uint64_t sum = 0;
  for(uint64_t i = 0; i < UPPER_LIMIT; i++) {
    sum += i * !(i % 3 && i % 5);
  }
  std::cout << sum << std::endl;
  return 0;
}
