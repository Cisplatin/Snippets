/*
    An implementation of the heapsort algorithm.
*/

template <typename T> class HeapSort {
    private:
        // Swaps the two indicies in the given array
        static void swap(T * array, int index_1, int index_2) {
            T buffer = array[index_1];
            array[index_1] = array[index_2];
            array[index_2] = buffer;
        }

        // Turns the subtree rooted at index into a heap satisfying the 
        // max-heap property - this assumes that the children of index are
        // both roots of max-heaps
        static void max_heapify(T * array, int size, int index) {
            // Find the values of the child nodes: messy if-loops are used
            // to minimize the number of comparisons and as a result have
            // a faster run-time. If no child exists, set it to one less than
            // the root, as to make sure it will be "less"
            T left, right;
            if(index * 2 + 1 < size) {
                left = array[index * 2];
                right = array[index * 2 + 1];
            } else if(index * 2 < size) {
                left = array[index * 2];
                right = array[index] - 1;
            } else {
                left = array[index] - 1;
                right = array[index] - 1;
            }

            // Find the maximum index and value
            T max_val, max_index;
            if(left < right) {
                max_val = right;
                max_index = index * 2 + 1;
            } else {
                max_val = left;
                max_index = index * 2;
            }

            // Determine if the current index is less than the max; if so,
            // swap and recursively max_heapify
            if(array[index] < max_val) {
                HeapSort<T>::swap(array, max_index, index);
                HeapSort<T>::max_heapify(array, size, max_index);
            }
        }

        // Turns the given array into a max-heap structure by calling
        // max_heapify on every node in reverse order
        static void build_max_heap(T * array, int size) {
            // Since the second half of elements are leaves, we only have
            // to heapify the first half of elements
            for(int i = size / 2 + 1; i >= 0; i--) {
                HeapSort<T>::max_heapify(array, size, i);
            }
        }
    public:
        // The sort function itself
        static void sort(T * array, unsigned int size) {
            // First turn the array into a max-heap
            HeapSort<T>::build_max_heap(array, size);

            // Extract elements one by one until sorted
            while(size > 0) {
                HeapSort<T>::swap(array, --size, 0);
                HeapSort<T>::max_heapify(array, size, 0);
            }
        }
};

#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;

int main() {
    // Generate a random array to test on
    srand(time(NULL));
    const int size = 10000000;
    int * my_array = new int[size];
    for(int i = 0; i < size; i++) {
        my_array[i] = rand() % size;
    }

    // Sort the array, time how long it takes
    clock_t start, end;
    start = clock();
    HeapSort<int>::sort(my_array, size);
    end = clock();
    
    // Print out the run-time of the sort
    cout << "Time to sort " << size << " elements: ";
    cout << ((float)end - (float)start) / CLOCKS_PER_SEC << " s" << endl;
    delete [] my_array;
    return 0;
}
