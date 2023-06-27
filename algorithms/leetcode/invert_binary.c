/* Definition for a binary tree node. */

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

struct TreeNode *invertTree(struct TreeNode *root) {
  // Invert
  if (root == NULL) {
    return NULL;
  }

  struct TreeNode *left = root->left;
  struct TreeNode *right = root->right;

  if (left != NULL) {
    invertTree(left);
  }

  if (right != NULL) {
    invertTree(right);
  }

  root->left = right;
  root->right = left;

  return root;
}
