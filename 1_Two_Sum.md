# Problem 1: Two Sum
*Level: easy*
## Description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.<br>You may assume that each input would have exactly one solution, and you may not use the same element twice.
## Solutions
### C, 16/17/2019
Analysis:
```c
int* twoSum(int* nums, int numsSize, int target, int *returnSize) {
    *returnSize = 2;
    int *res = malloc(*returnSize * sizeof(int));
    const int hsize = 2 * numsSize + 1;
    struct htab 
    {
        struct htab *next;
        int value;
        int index;
    } *htab[hsize];
    for (int i = 0; i < hsize; ++i)
    {
        htab[i] = malloc(sizeof(struct htab));
        htab[i]->next = NULL;
    }
    int hash;
    struct htab *p, *q;
    for (int i = 0; i < numsSize; ++i)
    {
        for (p = htab[(unsigned)nums[i] % hsize]; 
             p->next && p->value != nums[i]; p = p->next)
            ;
        if (p->next != NULL)
        {
            *res = p->index;
            *(res + 1) = i;
        }
        else
        {
            for (p = htab[(unsigned)(target - nums[i]) % hsize]; p->next; p = p->next)
                ;
            p->next = malloc(sizeof(struct htab));
            p->next->next = NULL;
            p->value = target - nums[i];
            p->index = i;
        }
    }
    for (int i = 0; i < hsize; ++i)
    {
        for (p = htab[i]; p->next; p = q)
        {
            q = p->next;
            free(p);
        }
        free(p);
    }
    return res;
}
```
Comments: