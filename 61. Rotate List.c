/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next || k == 0) 
        return head;

    struct ListNode* tail = head;
    int len = 1;
    while (tail->next) {
        tail = tail->next;
        len++;
    }

    tail->next = head;
    k = k % len;
    int step = len - k;
    struct ListNode* newtail = head;
    for (int i = 1; i < step; i++) 
        newtail = newtail->next;

    struct ListNode* newhead = newtail->next;
    newtail->next = NULL;
    return newhead;
}
