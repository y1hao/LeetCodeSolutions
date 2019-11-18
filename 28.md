# Problem 28: Implement strStr()
*Level: easy*
## Description
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
## Solutions
### C, 18/11/2019
Analysis:
```c
int strStr(char * haystack, char * needle){
    if (*needle == '\0')
        return 0;
    char *cur, *exp;
    int pos;
    for (pos = 0; haystack[pos] != '\0'; ++pos)
    {
        exp = needle;
        cur = haystack + pos;
        while (*exp == *cur)
        {
            if (*exp == '\0')
                return pos;
            ++exp;
            ++cur;
        }
        if (*exp == '\0')
            return pos;
        if (*cur == '\0')
            return -1;
    }
    return -1;
}


```
Comments: