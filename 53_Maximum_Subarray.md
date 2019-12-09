# Problem 53: Maximum Subarray
*Level: easy*
## Description
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**
```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
**Follow up:**

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solutions
### C, 18/11/2019
Analysis:
```c
int maxSubArray(int* nums, int numsSize){
    int max = *nums;
    int cur = 0;
    for (int i = 0; i < numsSize; ++i)
    {
        if (cur > 0 && cur + nums[i] > 0)
            cur += nums[i];
        else
            cur = nums[i];
        max = max > cur ? max : cur;
    }
    return max;
}
```
Comments: