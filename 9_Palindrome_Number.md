# Problem 9: Palindrome Number
*Level: easy*
## Description
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
## Solutions
### C, 16/11/2019
Analysis:
```c
bool isPalindrome(int x) {
    if (x < 0 || x % 10 == 0 && x)
        return false;
    int r = 0;
    while (x > r)
    {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r == x || r / 10 == x;
}
```
Comments: