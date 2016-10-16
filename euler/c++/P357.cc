/*
  Prime Generating Integers
  Problem 357
*/

#include <unordered_set>
#include <iostream>

const uint64_t UPPER_LIMIT = 100000001;
const uint64_t LOWEST_PRIME = 2;

int main(int argv, char * argc[]) {
  // We first generate a list of primes up to UPPER_LIMIT using the sieve of Eratosthenes
  bool * erato = new bool[UPPER_LIMIT + 1]();
  std::unordered_set <uint64_t> primes;
  for(uint64_t i = LOWEST_PRIME; i <= UPPER_LIMIT; i++) {
    if(erato[i]) continue;
    primes.insert(i);
    for(uint64_t j = i * i; j <= UPPER_LIMIT; j += i) erato[j] = true;
  }

  // We then make sure each factor of each number has all prime divisors, else we continue
  uint64_t total_sum = 0;
  bool * generating = new bool[UPPER_LIMIT + 1]();
  for(uint64_t i = 1; i <= UPPER_LIMIT; i++) {
    // First make sure that the number was not already checked. If not, we add it to the sum.
    if(!generating[i]) total_sum += i;

    // We then go through each multiple and check if the number is prime. We can check from i * 2
    // since we have already added i to our sum.
    for(uint64_t j = i + i, factor = 2; j <= UPPER_LIMIT; j += i, factor++) {
      generating[j] |= primes.find(i + factor) == primes.end();
    }
  }

  // Print the final result and collect the garbage
  std::cout << total_sum << std::endl;
  delete [] generating;
  delete [] erato;
  return 0;
}
