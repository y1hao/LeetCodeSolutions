# Problem 88: Merge Sorted Array
*Level: easy*
## Description
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

**Note:**

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

**Example:**
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## Solutions
### C, 19/11/2019
Analysis:
```c
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int buf[m + n];
    int i = 0, j = 0, k = 0;
    while (i < m && j < n)
        if (nums1[i] < nums2[j])
            buf[k++] = nums1[i++];
        else
            buf[k++] = nums2[j++];
    while(i < m)
        buf[k++] = nums1[i++];
    while(j < n)
        buf[k++] = nums2[j++];
    for (k = 0; k < m + n; ++k)
        nums1[k] = buf[k];
}
```
Comments: