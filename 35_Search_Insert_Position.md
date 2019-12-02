# Problem 35: Search Insert Position
*Level: easy*
## Description
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
## Solutions
### C, 18/11/2019
Analysis:
```c
int searchInsert(int* nums, int numsSize, int target){
    int i = 0;
    while (i < numsSize && nums[i] < target)
        ++i;
    return i;
}

```
Comments: