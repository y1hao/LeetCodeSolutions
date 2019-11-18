# Problem 26: Remove Duplicates form Sorted Array
*Level: easy*
## Description
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
## Solutions
### C, 18/11/2019
Analysis:
```c
int removeDuplicates(int* nums, int numsSize){
    int len = numsSize;
    if (len == 0) 
        return len;
    int pos = 0,
        begin = 0, 
        cur = *nums,
        diff;
    for (; pos < len; ++pos)
        if (nums[pos] != cur)
        {
            if ((diff = pos - begin - 1) > 0)
                for (int i = begin + 1; i < len - diff; ++i)
                    nums[i] = nums[i + diff];
            pos -= diff;
            begin = pos;
            cur = nums[pos];
            len -= diff;
            --pos;
        }
    if ((diff = pos - begin - 1) > 0)
        len -= diff;
    return len;
}
```
Comments: