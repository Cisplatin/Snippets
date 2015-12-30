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
            return;
        }

        // Turns the subtree rooted at index into a heap satisfying the 
        // max-heap property - this assumes that the children of index are
        // both roots of max-heaps
        static void max_heapify(T * array, int size, int index) {
            // Find the values of the child nodes
            T left = (index * 2 < size) ? array[index * 2] : array[index] - 1;
            T right = (index * 2 + 1 < size) ? array[index * 2 + 1] : array[index] - 1;
            T max = (left < right) ? right : left;
            T max_index = (left < right) ? index * 2 + 1 : index * 2;

            // Determine if the current index is less than the max; if so,
            // swap and recursively max_heapify
            if(array[index] < max) {
                HeapSort<T>::swap(array, max_index, index);
                HeapSort<T>::max_heapify(array, size, max_index);
            }
            return;
        }

        // Turns the given array into a max-heap structure by calling
        // max_heapify on every node in reverse order
        static void build_max_heap(T * array, int size) {
            for(int i = size - 1; i >= 0; i--) {
                HeapSort<T>::max_heapify(array, size, i);
            }
            return;
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
            return;
        }
};

#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;

int main() {
    // Generate a random array to test on
    srand(time(NULL));
    const int size = 10;
    int * my_array = new int[size];
    cout << "Array before sorting:" << endl;
    for(int i = 0; i < size; i++) {
        cout << (my_array[i] = rand() % size) << " ";
    }
    cout << endl;

    // Sort the array
    HeapSort<int>::sort(my_array, size);

    // Print out the sorted array
    cout << "Array after sorting:" << endl;
    for(int i = 0; i < size; i++) {
        cout << my_array[i] << " ";
    }
    cout << endl;
    delete [] my_array;
    return 0;
}
