# Problem 3: Longest Substring Without Repeating Characters
*Level: medium*
## Description
Given a string, find the length of the longest substring without repeating characters.
## Solutions
### C, 2/12/2019
Analysis:
```c
int lengthOfLongestSubstring(char * s){
    int len = strlen(s);
    if (len == 0)
        return 0;
    bool occur[256];
    for (int i = 0; i < 256; ++i)
        occur[i] = false;
    int end[len];
    for (int i = 0; i < len; ++i)
        end[i] = i + 1;
    int i, j, max = 0;
    for (i = 0; i < len; ++i)
    {
        occur[s[i]] = true;
        for (j = end[i]; j <= len; ++j)
        {
            if (j == len || occur[s[j]]) 
            {
                for (int k = i; k < j; ++k)
                    end[k] = j;
                break;
            }
            else
                occur[s[j]] = true;
        }
        occur[s[i]] = false;
    }
    for (i = 0; i < len; ++i)
        max = end[i] - i > max ? end[i] - i : max;
    return max;
}
```
Comments: