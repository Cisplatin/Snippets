/*
  Sum of totients of powers
  Problem 512
*/

#include <iostream>

const uint64_t UPPER_BOUND = 500000001;
const uint64_t LOWER_PRIME = 2;

int main(int argc, char * argv[]) {
  // We first calculate the value of Euler's totient function for all numbers less than UPPER_BOUND
  // To do this, we use a modified sieve of eratosthenes. We set unknown values to zero.
  // We also keep an entry of the smallest prime divisor for later use, for composite numbers.
  uint64_t * totient = new uint64_t[UPPER_BOUND];
  uint64_t * factors = new uint64_t[UPPER_BOUND];

  for(uint64_t prime = LOWER_PRIME; prime < UPPER_BOUND; prime++) {
    // Skip all composite numbers (i.e. there factors holds some prime)
    if(!factors[prime]) {

      // Since `prime` is a prime number, we can set the totient value now (as p - 1)
      totient[prime] = prime - 1;

      // Set all multiples to hold this prime as a factor
      for(uint64_t composite = prime * prime; composite < UPPER_BOUND; composite += prime) {
        factors[composite] = prime;
      }
    }
  }

  // Through some arithmetic, we find that f(n) = p(n)(1 + n + n^2 + ... + n^(n - 1))
  // For even powers of n, n^k = 1 (mod n + 1)
  // For odd powers of n, n^k = -1 (mod n + 1)
  // Thus the series alternates between 1 and 0. If (n - 1) is even, then it equals 1; else, it's 0.
  //
  // Therefore, f(n) = / phi(n) if n is odd
  //                   \    0   if n is even

  // We initalize total_sum at 1 so that we can skip the weird case of f(1)
  uint64_t total_sum = 1;
  for(uint64_t n = LOWER_PRIME; n < UPPER_BOUND; n++) {
    // If it's a prime number, we already have the totient value
    if(!totient[n]) {
      // First we find the totient of this value. We already have a prime divisor in factors, so
      // we use this to find a co-prime number.
      uint64_t divisor = n;
      do divisor /= factors[n];
      while(divisor % factors[n] == 0);

      // If divisor == 1, we found a prime power. We use the fact that phi(p^k) = p^k - p^(k - 1).
      // Otherwise, we calculate the totient value via multiplication.
      if(divisor == 1) totient[n] = (factors[n] - 1) * (n / factors[n]);
      else             totient[n] = totient[divisor] * totient[n / divisor];
    }

    // If the value of n is odd, we add it to our total sum
    if(n % 2) total_sum += totient[n] % (n + 1);
  }

  // Garbage collection and print the final answer
  std::cout << total_sum << std::endl;
  delete [] totient;
  delete [] factors;

  return 0;
}
