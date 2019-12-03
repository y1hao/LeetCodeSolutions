# Problem 4: Median of Two Sorted Arrays
*Level: hard*
## Description
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

**Example 1:**
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```
**Example 2:**
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```
## Solutions
### C, 2/12/2019
Analysis:
```c
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int count = nums1Size + nums2Size;
    int n = count / 2 + (count & 0x1), n1 = 0, n2 = 0;
    double res = 0.0;
    int cur;
    for (; n > 0; --n)
        if (n1 == nums1Size)
            cur = nums2[n2++];
        else if (n2 == nums2Size)
            cur = nums1[n1++];
        else
            cur = nums1[n1] < nums2[n2] ? nums1[n1++] : nums2[n2++];
    res = cur;
    if (!(count & 0x1))
    {
        if (n1 == nums1Size)
            res += nums2[n2];
        else if (n2 == nums2Size)
            res += nums1[n1];
        else 
            res += nums1[n1] < nums2[n2] ? nums1[n1] : nums2[n2];
        res /= 2;
    }
    return res;
}

```
Comments: