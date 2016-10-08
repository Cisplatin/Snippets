/*
    Divisibility of Factorials
    Problem 549
*/

#include <iostream>

const uint64_t LOWER_LIMIT = 2;
const uint64_t UPPER_LIMIT = 100000000;

int main(int argc, char * argv[]) {

    // Initialize the minimum value of each to zero. We then iterate over each
    // value and set it to the correct one.
    uint64_t * smallest = new uint64_t[UPPER_LIMIT + 1]();
    for(uint64_t prime = LOWER_LIMIT; prime <= UPPER_LIMIT; prime++) {
        // If the value is not zero, it's not a prime and so we skip it
        if(smallest[prime]) continue;
        uint64_t c_power = 1, c_value = prime;
        uint64_t p_found = 1, minimum = prime;

        while(c_value <= UPPER_LIMIT) {
            // Get the new minimum value given the power increase
            while(c_power > p_found) {
                uint64_t new_factor = (minimum += prime);
                do p_found++;
                while((new_factor /= prime) % prime == 0);
            }

            // Flag all multiples of the prime power with the new value
            for(uint64_t j = c_value; j <= UPPER_LIMIT; j += c_value)
                smallest[j] = smallest[j] < minimum ? minimum : smallest[j];
            c_power++;
            c_value *= prime;
        }
    }

    // Calculate and print the sum
    uint64_t total_sum = 0;
    for(uint64_t i = 0; i <= UPPER_LIMIT; i++) total_sum += smallest[i];
    delete [] smallest;
    std::cout << total_sum << std::endl;

    return 0;
}
