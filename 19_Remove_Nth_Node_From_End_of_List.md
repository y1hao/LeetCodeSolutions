# Problem 19: Remove Nth Node From End of List
*Level: medium*
## Description
Given a linked list, remove the n-th node from the end of list and return its head.

**Example:**
```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```
**Note:**

Given n will always be valid.

**Follow up:**

Could you do this in one pass?

## Solutions
### C, 7/12/2019
Analysis:
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *q = head, **p = &head;
    for (int i = 0; i < n; ++i)
        q = q->next;
    while (q)
    {
        q = q->next;
        p = &(*p)->next;
    }
    struct ListNode *tmp;
    tmp = *p;
    *p = (*p)->next;
    free(tmp);
    return head;
}

```
Comments: