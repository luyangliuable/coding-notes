void sortColors(int *nums, int numsSize) {
  // Beats 100%
  // Use count sort
  // Forgot the sorting part where you put the numbers back into the array (nums)
  // should be outside of the first for loo

  int count[3] = {0};

  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == 0) {
      count[0] += 1;
    } else if (nums[i] == 1) {
      count[1] += 1;
    } else {
      count[2] += 1;
    }
  }

  int i = 0;

  for (int j = 0; j < count[0]; j++) {
    nums[i] = 0;
    i++;
  }

  for (int j = 0; j < count[1]; j++) {
    nums[i] = 1;
    i++;
  }

  for (int j = 0; j < count[2]; j++) {
    nums[i] = 2;
    i++;
  }
}
