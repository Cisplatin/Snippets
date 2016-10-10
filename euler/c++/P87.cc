/*
  Prime Power Triples
  Problem 87
*/

#include <iostream>
#include <vector>
#include <set>
#include <math.h>

const int UPPER_LIMIT = 50000000;

int main(int argv, char * argc[]) {
  // We only need to check up to sqrt(UPPER_LIMIT), since the lowest one will always be squared
  int upper_limit = sqrt(UPPER_LIMIT);
  std::vector<uint64_t> squares, cubes, biquadratics;

  // Initialize an array to run the sieve of eratosthenes
  bool sieve[upper_limit];
  for(int i = 0; i < upper_limit; i++) sieve[i] = false;

  // For each prime number, run the sieve algorithm
  int total_primes = 0;
  for(int64_t i = 2; i < upper_limit; i++) {
    if(sieve[i]) continue;
    total_primes++;
    squares.push_back(i * i);
    cubes.push_back(i * i * i);
    biquadratics.push_back(i * i * i * i);
    for(int j = i * i; j < upper_limit; j += i) sieve[j] = true;
  }

  // We save each found solution so that we avoid duplicates
  std::set<int> found;

  // Go through each possibility and continue until we are finished
  int i = 0, j = 0, k = 0;
  bool finished = false;
  while(!finished) {
    // If our combination is less than the limit, add it to our set of solutions
    uint64_t next = squares.at(i) + cubes.at(j) + biquadratics.at(k);
    if(next < UPPER_LIMIT) found.insert(next);

    // Update the next set of integers to add
    if(++k == total_primes || next > UPPER_LIMIT) {
      if((k = 0) || ++j == total_primes) finished = (j = 0) || ++i == total_primes;
    }
  }

  // Print out the final answer, which is the number of keys in found
  std::cout << found.size() << std::endl;
  return 0;
}
