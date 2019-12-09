# Problem 23: Merge Two Sorted Lists
*Level: hard*
## Description
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
#define swap(a,b) do{struct ListNode *t=(a);(a)=(b);(b)= t;}while(0)
void _sort(struct ListNode **heap, int index, int size)
{
    int top = index, left = 2 * index + 1, right = 2 * index + 2;
    if (left < size && heap[left]
        && (heap[top] == NULL || heap[top]->val > heap[left]->val))
        top = left;
    if (right < size && heap[right]
        && (heap[top] == NULL || heap[top]->val > heap[right]->val))
        top = right;
    if (top != index)
    {
        swap(heap[top], heap[index]);
        _sort(heap, top, size);
    }
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    if (listsSize == 0)
        return NULL;
    struct ListNode *heap[listsSize];
    struct ListNode head = {0, NULL}, *cur = &head;
    for (int i = 0; i < listsSize; ++i)
    {
        heap[i] = lists[i];
        if (lists[i])
            lists[i] = lists[i]->next;
    }
    for (int i = listsSize - 1; i >= 0; --i)
        _sort(heap, i, listsSize);
    struct ListNode *curEle;
    while ((curEle = *heap) != NULL)
    {
        *heap = curEle->next;
        cur->next = curEle;
        cur = cur->next;
        cur->next = NULL;
        _sort(heap, 0, listsSize);
    }
    return head.next;
}
#undef swap
```
Comments: