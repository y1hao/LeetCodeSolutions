# Problem 16: 3Sum_Closest
*Level: medium*
## Description
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
## Solutions
### C, 8/12/2019
Analysis:
```c
int threeSumClosest(int* nums, int numsSize, int target){
    int res = nums[0] + nums[1] + nums[2];
    int cursum;
    for (int i = 0; i <= numsSize - 3; ++i)
        for (int j = i + 1; j <= numsSize - 2; ++j)
            for (int k = j + 1; k <= numsSize - 1; ++k)
                if (abs((cursum = nums[i] + nums[j] + nums[k]) - target) < abs(res - target))
                    res = cursum;
    return res;
}
```
Comments: