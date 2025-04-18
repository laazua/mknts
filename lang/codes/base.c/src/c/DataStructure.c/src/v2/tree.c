// 二叉树

#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *new_tree_node(int data)
{
    struct TreeNode *TN = NULL;
    TN = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    if (TN == NULL) {
        fprintf(stderr, "TreeNode malloc failure!\n");
        return NULL;
    }

    TN->data = data;
    TN->left = NULL;
    TN->right = NULL;

    return TN;
}

struct TreeNode *insert_tree_node(struct TreeNode *root, int data)
{
    if (root == NULL) return new_tree_node(data);

    if (data <= root->data)
        root->left = insert_tree_node(root->left, data);
    else
        root->right = insert_tree_node(root->right, data);

    return root;
}

void inorder_traversal(struct TreeNode *root)
{
    if (root != NULL) {
        inorder_traversal(root->left);
        fprintf(stdout, "%d\n", root->data);
        inorder_traversal(root->right);
    }
}

void delete_tree_node(struct TreeNode *root)
{
    if (root != NULL) {
        free(root);
        root = NULL;
    }
}

int main() 
{
    struct TreeNode *root = NULL;
    root = insert_tree_node(root, 100);
    root = insert_tree_node(root, 245);
    root = insert_tree_node(root, 522);
    root = insert_tree_node(root, 785);
    root = insert_tree_node(root, 674);
    inorder_traversal(root);
    delete_tree_node(root);

    return 0;
}
