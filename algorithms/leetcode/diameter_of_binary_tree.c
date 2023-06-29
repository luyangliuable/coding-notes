
/* Definition for a binary tree node. */

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

#include <stdlib.h> // For malloc
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int *dfsBinaryTree(struct TreeNode *root);

int diameterOfBinaryTree(struct TreeNode *root) {
  // Beats 41%
  // without free() it is the same
  // Something was wrong in the define max
  if (root == NULL) {
    return 0;
  }

  int *r = dfsBinaryTree(root);
  int res = r[1];

  free(r);

  return res;
}

int *dfsBinaryTree(struct TreeNode *root) {
  int *r = malloc(sizeof(int) * 2);

  if (root == NULL) {
    r[0] = 0;
    r[1] = 0;
    return r;
  }

  int *right = dfsBinaryTree(root->right);
  int *left = dfsBinaryTree(root->left);

  r[0] = MAX(left[0], right[0]) + 1;

  r[1] = MAX(left[0] + right[0], MAX(left[1], right[1]));

  free(left);
  free(right);

  return r;
}
