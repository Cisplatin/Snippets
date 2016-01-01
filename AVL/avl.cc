#include <iostream>

template <class T> class Node {
    public:
        T data;
        Node<T> * right, * left;
        // Longest path from the node to a leaf
        int height;
        Node(T data) {
            this->data = data;
            // Since new nodes are inserted as leaves, they have no children
            this->right = NULL;
            this->left = NULL;
            // Since new nodes are inserted as leaves, their height is zero
            this->height = 0;
        }
};

/*
    An implementation of the AVL tree data structure.
*/
template <class T> class AVLTree {
    private:
        Node<T> * root;
        void deleteAllNodes(Node<T> * current) {
            if(current != NULL) {
                deleteAllNodes(current->left);
                deleteAllNodes(current->right);
                delete current;
            }
        }
        
        // Recursively finds where to insert the node into the tree. We treat
        // equal values as being "bigger" for the sake of consistency.
        void recursive_insert(T data, Node<T> * current) {
            // Find which child is of interest
            if(data < current->data) {
                if(current->left == NULL) current->left = new Node<T>(data);
                else this->recursive_insert(data, current->left);
            } else {
                if(current->right == NULL) current->right = new Node<T>(data);
                else this->recursive_insert(data, current->right);
            }
        }

        // Recursively recurses the tree and prints out the nodes
        void recursive_traverse(Node<T> * current) const {
            if(current != NULL) {
                this->recursive_traverse(current->left);
                std::cout << current->data << " ";
                this->recursive_traverse(current->right);
            }
        }
    public:
        // Normal implementations for constructor/destructor
        AVLTree() { this->root = NULL; }
        ~AVLTree() { this->deleteAllNodes(this->root); }
        
        // Inserts the given data into the tree
        void insert(T data) {
            // If the root is NULL, this data point makes up the tree
            if(this->root == NULL) {
                this->root = new Node<T>(data);
            // Otherwise, recursively find out where to place the node
            } else {
                this->recursive_insert(data, this->root);
            }
        }    

        // Traverses the tree and prints out the nodes in order
        void traverse() const {
            // Recursively traverse the left then the right
            this->recursive_traverse(this->root);
            std::cout << std::endl;
        }
};

int main() {
    // An example of the AVL tree in action
    AVLTree<int> * tree = new AVLTree<int>();
    // Insert a few elements
    tree->insert(3);
    tree->insert(2);
    tree->insert(4);
    // Traverse the tree
    tree->traverse();
    delete tree;
    return 0;
}
