#define max(a, b) (a < b ? b : a);

int trap(int *height, int heightSize) {
  // Beats 85.84% of users
  // accidentally redefined lm and rm in while loop because put int in front
  if ( heightSize == 0 ) {
    return 0;
  }

  int l = 0;
  int r = heightSize - 1;

  int lm = height[l];
  int rm = height[r];

  int res = 0;

  while (l < r) {
    if (lm < rm) {
      l += 1;
      lm = max(height[l], lm);
      res += lm - height[l];
    } else {
      r -= 1;
      rm = max(height[r], rm);
      res += rm - height[r];
    }
  }

  return res;
}
