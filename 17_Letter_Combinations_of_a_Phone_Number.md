# Problem 18: Letter Combimations of a Phone Number
*Level: medium*
## Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

**Example:**
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solutions
### C, 7/12/2019
Analysis:
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char *map[] = {
    NULL, NULL, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
};

char **letterCombinations(char *digits, int *returnSize){
    char **res = NULL;
    if (strlen(digits) == 0)
    {
        *returnSize = 0;
        return res;
    }
    if (strlen(digits) == 1)
    {
        *returnSize = strlen(map[*digits - '0']);
        res = malloc(sizeof(char *) * *returnSize);
        for (int i = 0; i < *returnSize; ++i)
        {
            res[i] = malloc(2);
            res[i][0] = map[*digits - '0'][i];
            res[i][1] = '\0';
        }
        return res;
    }
    int size;
    char **last = letterCombinations(digits + 1, &size);
    int len = strlen(map[*digits - '0']);
    *returnSize = len * size;
    res = malloc(sizeof(char *) * *returnSize);
    for (int i = 0; i < len; ++i)
    {
        char c = map[*digits - '0'][i];
        for (int j = 0; j < size; ++j)
        {
            int index = i * size + j;
            int lastlen = strlen(*last);
            res[index] = malloc(lastlen + 2);
            res[index][0] = c;
            res[index][1] = '\0';
            strcat(res[index], last[j]);
        }
    }
    for (int i = 0; i < size; ++i)
        free(last[i]);
    return res;
}

```
Comments: