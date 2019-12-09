# Problem 83: Remove Duplicates from Sorted List
*Level: easy*
## Description
Given a sorted linked list, delete all duplicates such that each element appear only once.

***Example 1:***
```
Input: 1->1->2
Output: 1->2
```
**Example 2:**
```
Input: 1->1->2->3->3
Output: 1->2->3
```

## Solutions
### C, 19/11/2019
Analysis:
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    if (head == NULL)
        return head;
    int cur = head->val;
    struct ListNode **p = &(head->next), *tmp;
    while (*p)
    {
        if ((*p)->val == cur)
        {
            tmp = *p;
            *p = (*p)->next;
            free(tmp);
        }
        else
        {
            cur = (*p)->val;
            p = &((*p)->next);
        } 
    }
    return head;
}

```
Comments: