# Problem 21: Merge Two Sorted Lists
*Level: easy*
## Description
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
## Solutions
### C, 18/11/2019
Analysis:
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode head = {.next = NULL}, *cur = &head;
    while (l1 && l2)
    {
        if (l1->val < l2->val)
        {
            cur->next = l1;
            l1 = l1->next;
        }
        else
        {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
    }
    while (l1)
    {
        cur->next = l1;
        l1 = l1->next;
        cur = cur->next;
    }
    while (l2)
    {
        cur->next = l2;
        l2 = l2->next;
        cur = cur->next;
    }
    cur->next = NULL;
    return head.next;
}


```
Comments: