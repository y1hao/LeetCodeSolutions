# Problem 14: Longest Common Prefix
*Level: easy*
## Description
 Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
**Example 1:**
```
Input: ["flower","flow","flight"]
Output: "fl"
```
**Example 2:**
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
**Note:**

All given inputs are in lowercase letters a-z.
## Solutions
### C, 18/11/2019
Analysis:
```c
#define MAX_LEN 256
char * longestCommonPrefix(char ** strs, int strsSize){
    char *res = malloc(MAX_LEN * sizeof(char));
    if (strsSize == 0)
    {
        *res = '\0';
        return res;
    }
    if (strsSize == 1)
    {
        strcpy(res, *strs);
        res[MAX_LEN - 1] = '\0';
        return res;
    }
    int i, j;
    char cur;
    for (i = 0; i < MAX_LEN - 1; ++i)
    {
        for (j = 0, cur = (*strs)[i]; 
             j < strsSize && strs[j][i] == cur && cur != '\0';
             ++j)
            ;
        if (j < strsSize || cur == '\0')
            break;
        res[i] = cur;
    }
    res[i] = '\0';
    return res;
}
```
Comments: