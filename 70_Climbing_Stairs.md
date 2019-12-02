# Problem 70: Climbing Stairs
*Level: easy*
## Description
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
## Solutions
### C, 19/11/2019
Analysis:
```c
int climbStairs(int n){
    int a = 1, b = 1, c;
    while (--n)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

```
Comments: