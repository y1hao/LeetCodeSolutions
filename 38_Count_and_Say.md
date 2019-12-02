# Problem 38: Count and Say
*Level: easy*
## Description
The count-and-say sequence is the sequence of integers with the first five terms as following:
|||
|-|-|
|1|     1|
|2|     11|
|3|     21|
|4|     1211|
|5|     111221|

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
## Solutions
### C, 18/11/2019
Analysis:
```c
#define BUFF_SIZE 10000

char * countAndSay(int n){
    char *res = NULL;
    if (n == 1)
    {
        res = malloc(sizeof(char) * 2);
        res[0] = '1';
        res[1] = '\0';
        return res;
    }
    char *prev = countAndSay(n - 1);
    char buff[BUFF_SIZE];
    char *p = prev, cur = *p, count = '0';
    int len = 0;
    for (; *p != '\0'; ++p)
    {
        if (*p != cur)
        {
            buff[len++] = count;
            buff[len++] = cur;
            cur = *p;
            count = '1';
        }
        else
            ++count;
    }
    buff[len++] = count;
    buff[len++] = cur;
    buff[len++] = '\0';
    res = malloc(len * sizeof(char));
    strcpy(res, buff);
    free(prev);
    return res;
}


```
Comments: