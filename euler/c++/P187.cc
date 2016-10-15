/*
  Semiprimes
  Problem 187
*/

#include <vector>
#include <iostream>

const uint64_t UPPER_LIMIT = 10000000;
const uint64_t LOWEST_PRIME = 2;
using namespace std;

// Returns the index of the prime number not exceeding the given maximum.
uint64_t prime_index(vector <uint64_t> * primes, uint64_t maximum, uint64_t start, uint64_t end) {
  uint64_t mid_point = (start + end) / 2;
  if((*primes)[end] <= maximum) return end + 1;
  else if(end - start <= 1) return start + 1;
  else if((*primes)[mid_point] > maximum) return prime_index(primes, maximum, start, mid_point);
  else return prime_index(primes, maximum, mid_point, end);
}

int main(int argc, char * argv[]) {
  // We generate a list of prime numbers using the sieve of Eratosthenes
  uint64_t total_sum = 0;
  vector <uint64_t> primes;
  bool * erato = new bool[UPPER_LIMIT]();

  // We only need to check up to UPPER_LIMIT / 2 as a maximum
  for(uint64_t i = LOWEST_PRIME; i < UPPER_LIMIT / 2; i++) {
    if(erato[i]) continue;
    primes.push_back(i);
    total_sum += prime_index(&primes, UPPER_LIMIT / i, 0, primes.size() - 1);
    for(uint64_t j = i * i; j < UPPER_LIMIT; j += i) erato[j] = true;
  }

  // Print out the final result and collect garbage
  cout << total_sum << endl;
  delete [] erato;
  return 0;
}
