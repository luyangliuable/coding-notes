/* Definition for a binary tree node. */

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

#include <limits.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))

long maxPathSumAux(struct TreeNode *root, long *max_ptr);

long maxPathSum(struct TreeNode *root) {
  // Beats 76%
  // Hard question but felt like an eaasy
  // Initially forgot to add root->val and added +1 instead
  // Decided to make use ptr for max instead of global variable
  // Learnt to use INT_MIN and didn't realise nodes can be negative.

  long max = INT_MIN;

  long r = maxPathSumAux(root, &max);

  if (max == INT_MIN)
    // This means all path are negative and contribute it to end up being negative. Just have NULL in subset
    return 0;

  // If only the root can give the largest path
  return MAX(max, root->val);
}

long maxPathSumAux(struct TreeNode *root, long *max_ptr) {
  if (root == NULL) {
    return 0;
  }

  long left = maxPathSumAux(root->left, max_ptr);
  long right = maxPathSumAux(root->right, max_ptr);

  // weight so add root->val
  *max_ptr = MAX(*max_ptr, left + right + root->val);

  // max that or 0 so we don't consider negative tree subsets
  return MAX( MAX(left, right) + root->val, 0);
}
