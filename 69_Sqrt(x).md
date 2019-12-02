# Problem 69: Sqtr()
*Level: easy*
## Description
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
## Solutions
### C, 19/11/2019
Analysis:
```c
int mySqrt(int x){
    return (int)sqrt(x);
}
```
Comments: