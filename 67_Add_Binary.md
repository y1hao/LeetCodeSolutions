# Problem 67: Add Binary
*Level: easy*
## Description
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```
**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Solutions
### C, 19/11/2019
Analysis:
```c
#define BUF_SIZE 2048
char * addBinary(char * a, char * b){
    int lena = strlen(a), lenb = strlen(b), i = 0, j = 0;
    char buf[BUF_SIZE], c = 0, *res = NULL;
    while (lena && lenb)
    {
        buf[i] = a[--lena] + b[--lenb] - '0'+ c;
        if (buf[i] > '1')
        {
            c = 1;
            buf[i] -= 2;
        }
        else
            c = 0;
        ++i;
    }
    while (lena)
    {
        buf[i] = a[--lena] + c;
        if (buf[i] > '1')
        {
            c = 1;
            buf[i] -= 2;
        }
        else
            c = 0;
        ++i;
    }
    while (lenb)
    {
        buf[i] = b[--lenb]+ c;
        if (buf[i] > '1')
        {
            c = 1;
            buf[i] -= 2;
        }
        else
            c = 0;
        ++i;
    }
    if (c)
        buf[i++] = c + '0';
    res = malloc((i + 1) * sizeof(char));
    while (--i >= 0)
        res[j++] = buf[i];
    res[j] = '\0';
    return res;
}
```
Comments: