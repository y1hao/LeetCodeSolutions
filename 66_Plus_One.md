# Problem 66: Plus One
*Level: easy*
## Description
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**
```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```
**Example 2:**
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```
## Solutions
### C, 18/11/2019
Analysis:
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define BUFF_SIZE 10000
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int len = 0, carry = 1;
    int buff[BUFF_SIZE];
    while (--digitsSize >= 0)
    {
        buff[len] = digits[digitsSize] + carry;
        if (buff[len] > 9)
        {
            buff[len] -= 10;
            carry = 1;
        }
        else 
            carry = 0;
        len++;
    }
    if (carry)
        buff[len++] = 1;
    *returnSize = len;
    int *res = malloc(len * sizeof(int));
    int i = 0;
    while (--len >= 0)
        res[len] = buff[i++];
    return res;
}
```
Comments: