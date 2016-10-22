/*
  Divisor Square Sum
  Problem 211
*/

#include <vector>
#include <numeric>
#include <iostream>
#include <math.h>

const uint64_t UPPER_LIMIT = 64000000;

int main(int argv, char * argc[]) {
  // We start the sum at one so that we can skip one, to make generalizations easier
  uint64_t sum = 1;
  std::vector<uint64_t> sieve(UPPER_LIMIT + 1);
  for(uint64_t i = 2; i <= UPPER_LIMIT; i++) {
    // If it's a prime number, check the multiples properly
    if(sieve[i] == 0) {
      // Set the value for this prime, which is p^2 + 1
      sieve[i] = i * i + 1;

      // Go through every multiple of the prime and multiply by the proper amount. We have to make
      // sure that we get the powers of i as well, so we keep a power count. Note that for
      // powers of primes, the value is (1 - p^(2n + 2))/(1 - p^2)
      uint64_t current = i, value = sieve[i], numer = i * i * i * i;
      while(current <= UPPER_LIMIT) {
        for(uint64_t j = current, factor = 1; j <= UPPER_LIMIT; j += current, factor++) {
          // Skip anything that is of a larger power
          if(factor % i == 0) continue;

          // If it's zero, set it to one then multiply. Otherwise just multiply.
          if(sieve[j] == 0)   sieve[j] = value;
          else if(i != j)     sieve[j] *= value;
        }

        // Update the new values
        current *= i;
        value = ((numer *= i * i) - 1) / (sieve[i] - 2);
      }
    }

    // Add the value to the total sum if it's a perfect square.
    uint64_t root = sqrt(sieve[i]);
    if(root * root == sieve[i]) sum += i;
  }
  std::cout << sum << std::endl;
  return 0;
}
