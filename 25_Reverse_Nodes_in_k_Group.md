# Problem 25: Reverse Nodes in k-Group
*Level: hard*
## Description
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

**Example:**

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

**Note:**

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.


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

struct ListNode* reverseKGroup(struct ListNode* head, int k){
    if (k < 2)
        return head;
    struct ListNode **beg = &head, *end, **tpp, *front, *rear, *tmp;
    while (*beg)
    {
        end = *beg;
        int i = 0;
        for (; i < k - 1 && end->next; ++i)
            end = end->next;
        if (i < k - 1)
            return head;
        front = *beg;
        rear = front->next;
        (*beg)->next = end->next;
        tpp = &((*beg)->next);
        for (;rear != end; front = rear, rear = tmp)
        {
            tmp = rear->next;
            rear->next = front;
        }
        rear->next = front;
        *beg = end;
        beg = tpp;
    }
    return head;
}
```
Comments: