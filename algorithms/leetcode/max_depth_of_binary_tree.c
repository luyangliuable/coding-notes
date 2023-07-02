/* Definition for a binary tree node. */

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

#define MAX(x, y) (((x) > (y)) ? (x) : (y))


struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int maxDepth(struct TreeNode *root) {
  // INitially confused because the depth don't add update
  // So count depth by nodes not links
  // Beats 100%
  // Do so by checking if current root pointing is null not left and right are null
  if (root == NULL) {
    return 0;
  }

  int a = maxDepth(root->left);
  int b = maxDepth(root->right);

  return MAX(a, b) + 1;
}
