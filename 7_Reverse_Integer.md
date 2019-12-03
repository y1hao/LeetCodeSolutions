# Problem 7: Reverse Integer
*Level: easy*
## Description
Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
```
Input: 123
Output: 321
```
**Example 2:**
```
Input: -123
Output: -321
```
**Example 3:**
```
Input: 120
Output: 21
```
**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Solutions
### C, 16/11/2019
Analysis:
```c
#define POS_OVERFLOW (INT_MAX - INT_MAX / 10 * 10)
#define NEG_OVERFLOW (INT_MIN - INT_MIN / 10 * 10)
int reverse(int x){
    int r = 0, pop;
    while (x)
    {
        pop = x % 10;
        if (r > INT_MAX / 10 || r == INT_MAX / 10 && pop > POS_OVERFLOW)
            return 0;
        if (r < INT_MIN / 10 || r == INT_MIN / 10 && pop < NEG_OVERFLOW)
            return 0;
        r = r * 10 + pop;
        x /= 10;
    }
    return r;
}
```
Comments: