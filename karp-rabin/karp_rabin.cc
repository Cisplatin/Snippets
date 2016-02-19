#include <string>

int karp_rabin(std::string * s, std::string * t) {
    /*
    An implementation of the karp-rabin algorithm as demonstrated by
    Erik Demaine in MIT's 6.006 OCW material. The algorithm returns -1 if
    the string s is not a substring of t, and returns the index of the first
    character of the first instance if it is a substring.
    
    This algorithm runs in time O(|s| + |t|)
    */
    
    // We keep a rolling hash for both s and t so that the hash values of each
    // s-length substring of t does not have to be completely recomputed. The
    // rolling hash uses the division method base 128 (since all strings are
    // assumed to be ASCII).
    const int STR_BASE = 128;

    // We also need a prime number to keep our division method a constant time
    // amortized positive result (i.e. less collisions). Note that there is
    // a maximum number of bits for an int too which will be module a 
    // Mersenne Prime, so no manual modulus is required.
    
    // We first calculate the rolling hash of s and t. Note that according to
    // the C++ standard, s->length() is a constant complexity function, so
    // no harm by placing it in the for-condition. We use a variant of the
    // Rabin fingerprint rolling hash
    int hash_s = 0, hash_t = 0, multiplier = 1;
    for(int i = s->length() - 1; i >= 0; i--) {
        hash_s += (*s)[i] * multiplier;
        hash_t += (*t)[i] * multiplier;
        multiplier *= STR_BASE;
    }

    // Re-adjust the multiplier for ease of us when adding new digits later
    multiplier /= STR_BASE;

    // First check if the substring is found at the first index
    if(hash_s == hash_t) {
        // If the hashes are equal, there is a small chance the strings are
        // still different, so we check this
        bool found_substr = true;
        for(unsigned int i = 0; i < s->length(); ++i) {
            // Found a character that doesn't match, so nevermind
            if((*s)[i] != (*t)[i]) {
                found_substr = false;
                i = s->length();
            }
        }
        // If no unmatching characters were found, the result is found!
        if(found_substr) return 0;
    }

    // Start the rolling hash across t to find the substring
    for(unsigned int i = s->length(); i < t->length(); ++i) {
        // Update the rolling hash of t by removing the first digit, and then
        // add the new digit
        hash_t = STR_BASE * (hash_t - (multiplier * (*t)[i - s->length()]));
        hash_t = (hash_t + (*t)[i]);
        // If the hashes are equal, as above, we check string equality
        if(hash_t == hash_s) {
            bool found_substr = true;
            for(unsigned int j = 0; j < s->length(); ++j) {
                if((*s)[j] != (*t)[j + i - s->length() + 1]) {
                    found_substr = false;
                    j = s->length();
                }
            }
            if(found_substr) return (i - s->length() + 1);
        }
    }
    // No substrings were found so we return -1
    return -1;
}

#include <iostream>
#include <time.h>
using namespace std;

int main() {
    /*
        An example of use for the karp-rabin algorithm. We load a file which
        contains randomly generated Latin
    */
    std::string pattern = "ab";
    std::string document = "Karp-Rabin Algorithm";

    // Time how long it takes to find the substring
    clock_t start, end;
    start = clock();
    int result = karp_rabin(&pattern, &document);
    end = clock();

    // Print out the result
    cout << "Found substring at index " << result << " in ";
    cout << ((float)end - (float)start) << " cycles" << endl;
    return 0;
}
