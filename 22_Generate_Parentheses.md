# Problem 22: Generate Parentheses
*Level: medium*
## Description
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```
## Solutions
### C, 9/12/2019
Analysis:
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void _makePair(char *resbuf, int *rbp, bool *buf, int total, int index, int remain, int unmatched)
{
    if (index == total && unmatched == 0)
    {
        char *cur = resbuf + *rbp;
        for (int i = 0; i < total; ++i)
            cur[i] = buf[i] ? '(' : ')';
        *rbp += total;
        return;
    }
    else if (unmatched < 0 || remain < 0)
        return;
    buf[index] = true;
    _makePair(resbuf, rbp, buf, total, index + 1, remain - 1, unmatched+1);
    buf[index] = false;
    _makePair(resbuf, rbp, buf, total, index + 1, remain, unmatched - 1);
}

char ** generateParenthesis(int n, int* returnSize){
    bool buf[n * 2];
    char resbuf[50000];
    char **res = NULL;
    int rbp = 0;
    _makePair(resbuf, &rbp, buf, 2 * n, 0, n, 0);
    *returnSize = rbp / 2 / n;
    res = malloc(*returnSize * sizeof(char *));
    for (int i = 0; i < *returnSize; ++i) 
    {
        char *cur = malloc(2 * n + 1);
        memcpy(cur, &resbuf[i * 2 * n], 2 * n);
        cur[2 * n] = '\0';
        res[i] = cur;
    }
    return res;
}
```
Comments: