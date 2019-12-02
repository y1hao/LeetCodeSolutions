# Problem 100: Same Tree
*Level: easy*
## Description
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
## Solutions
### C, 20/11/2019
Analysis:
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if (p == NULL && q == NULL)
        return true;
    if (p == NULL || q == NULL)
        return false;
    return isSameTree(p->left, q->left)
        && isSameTree(p->right, q->right)
        && (p->val == q->val);
}
```
Comments: