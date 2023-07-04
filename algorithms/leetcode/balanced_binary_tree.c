/* Definition for a binary tree node. */

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

#include <math.h>
#include <stdlib.h> // For malloc
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int binaryTreeDfs(struct TreeNode *node);

int balanced = 1; // global variable

int isBalanced(struct TreeNode *root) {
  // Beats 90% of submissions
  // Decided to use global variable to keep track if balanced can't stop early
  // forgot abs(left - right) > 1 not abs(left - right) >= 1 on line 23
  // Need to reset balanced = 1 for leetcode

  balanced = 1;

  if (root == NULL)
    return 1;

  int left = binaryTreeDfs(root->left);
  int right = binaryTreeDfs(root->right);

  if (abs(left - right) <= 1) {
    return balanced;
  }

  return 0;
}

int binaryTreeDfs(struct TreeNode *node) {
  if (node == NULL)
    return 0;

  int left = binaryTreeDfs(node->left);
  int right = binaryTreeDfs(node->right);

  if (abs(left - right) > 1) {
    balanced = 0;
  }

  return MAX(left, right) + 1;
}
