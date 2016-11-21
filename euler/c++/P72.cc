/*
  Counting Fractions
  Problem 72
*/

#include <map>
#include <iostream>

const uint64_t UPPER_LIMIT = 1000000;
const uint64_t LOWEST_PRIME = 2;

// What kind of language doesn't have the gcd function built int?
uint64_t gcd(uint64_t a, uint64_t b) {
    return b ? gcd(b, a % b) : a;
}

int main(int argc, char *argv[]) {
  // The question is equivalent to finding the size of the UPPER_LIMIT'th Farey sequence.
  // Note that F_n = F_{n-1} + phi(n). So we continue this until we reach UPPER_LIMIT
  // We start with the first Farey sequence, which has two elements - 0 and 1. Note however that
  // we only want numbers between 0 and 1 exclusively. Thus we remove these elements.
  uint64_t farey_size = 0;

  // We know the totient value of 1 is 1, so we add that as a base case.
  std::map<uint64_t, uint64_t> totient;
  totient.insert(std::pair<uint64_t, uint64_t>(1, 1));

  // To find the value of the phi function, we use a sieve of eratosthenes.
  bool * sieve = new bool[UPPER_LIMIT + 1]();
  for(uint64_t prime = LOWEST_PRIME; prime <= UPPER_LIMIT; prime++) {
    if(sieve[prime]) continue;

    // Note that the totient values of a prime p is p - 1.
    totient.insert(std::pair<uint64_t, uint64_t>(prime, prime - 1));
    for(uint64_t composite = prime * prime; composite <= UPPER_LIMIT; composite += prime) {
      sieve[composite] = true;
    }
  }

  // We now find each successive Farey size and compute the totient function as we go. We start
  // from 2 since we already have the size of the first Farey sequence.
  for(uint64_t k = LOWEST_PRIME; k <= UPPER_LIMIT; k++) {

    // We now find the totient value for n. If it's prime, we just add the known value. Otherwise,
    // we calculate the totient based off of the first divisor that we find.
    if(totient.find(k) == totient.end()) {

      // Find the lowest divisor of this composite number k.
      uint64_t factor = LOWEST_PRIME;
      while(k % factor) factor++;

      // Apply the formula with the found factor and add it to our map. We also need the other
      // factor found by dividing k by factor.
      uint64_t other = k / factor;
      uint64_t greatest = gcd(factor, other);
      uint64_t value = totient.at(factor) * totient.at(other) * greatest / totient.at(greatest);
      totient.insert(std::pair<uint64_t, uint64_t>(k, value));
    }

    // Now that we have the totient value, we add it to our sum.
    farey_size += totient.at(k);
  }

  // Print out the final size of the farey sequence
  std::cout << farey_size << std::endl;
  return 0;
}
