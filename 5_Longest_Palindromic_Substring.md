# Problem 5: Longest Palindromic Substring
*Level: medium*
## Description
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
## Solutions
### C, 2/12/2019
Analysis:
```c
char * longestPalindrome(char * s){
    int len = strlen(s);
    int beg = 0, max = 1;
    for (int i = 0; i <= len - max; ++i)
    {
        for (int j = i + max; j < len; ++j)
        {
            int k;
            for (k = 0; i + k < j - k; ++k)
                if (s[i + k] != s[j - k])
                    break;
            if (i + k >= j - k && j - i + 1 > max)
            {
                beg = i;
                max = j - i + 1;
            }
        }
    }
    char *res = malloc(max + 1);
    strncpy(res, &s[beg], max);
    res[max] = '\0';
    return res;
}
```
Comments: