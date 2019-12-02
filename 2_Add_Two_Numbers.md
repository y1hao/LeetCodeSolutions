# Problem 2: Add Two Numbers
*Level: medium*
## Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
## Solutions
### C, 2/12/2019
Analysis:
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *p1 = l1, *p2 = l2, head = {0, NULL}, *cur = &head;
    int carry = 0, v1, v2;
    for (; p1 || p2 || carry; p1 && (p1 = p1->next), p2 && (p2 = p2->next))
    {
        v1 = p1 ? p1->val : 0;
        v2 = p2 ? p2->val : 0;
        carry += v1 + v2;
        struct ListNode *p = malloc(sizeof (struct ListNode));
        p->val = carry % 10;
        carry /= 10;
        p->next = NULL;
        cur->next = p;
        cur = cur->next;
    }
    return head.next;
}
```
Comments: