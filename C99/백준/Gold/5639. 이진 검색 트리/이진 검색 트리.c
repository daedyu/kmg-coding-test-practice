#include <stdio.h>

struct BinaryNode
{
    int key;
    struct BinaryNode *left;
    struct BinaryNode *right;
};

int main() {
    char line[1024];

    struct BinaryNode root = {0, NULL, NULL};

    while (fgets(line, sizeof(line), stdin) != NULL) {
        line[strcspn(line, "\n")] = '\0';
        int key = atoi(line);
        if (root.key == 0) {
            root.key = key;
        } else {
            struct BinaryNode *parent = &root;
            while (parent->key != NULL) {
                if (parent->key > key) {
                    if (parent->left == NULL) {
                        parent->left = malloc(sizeof(struct BinaryNode));
                        parent->left->key = key;
                        parent->left->left = NULL;
                        parent->left->right = NULL;
                        break;
                    } else {
                        parent = parent->left;
                    }
                } else {
                    if (parent->right == NULL) {
                        parent->right = malloc(sizeof(struct BinaryNode));
                        parent->right->key = key;
                        parent->right->left = NULL;
                        parent->right->right = NULL;
                        break;
                    } else {
                        parent = parent->right;
                    }
                }
            }
        }
    }
    printOrder(&root);

    return 0;
}

void printOrder(struct BinaryNode *node) {
    if (node == NULL) {
        return;
    }
    printOrder(node->left);
    printOrder(node->right);
    printf("%d\n", node->key);
}