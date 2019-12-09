# Problem 24: Swap Nodes in Pairs
*Level: medium*
## Description
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


**Example:**
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## Solutions
### C, 9/12/2019
Analysis:
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode **pp = &head, *q, **tmp;
    while (*pp && (*pp)->next)
    {
        q = (*pp)->next;
        (*pp)->next = q->next;
        tmp = &((*pp)->next);
        q->next = *pp;
        *pp = q;
        pp = tmp;
    }
    return head;
}
```
Comments: