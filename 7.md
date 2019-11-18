# Problem 7: Reverse Integer
*Level: easy*
## Description
> Given a 32-bit signed integer, reverse digits of an integer.
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