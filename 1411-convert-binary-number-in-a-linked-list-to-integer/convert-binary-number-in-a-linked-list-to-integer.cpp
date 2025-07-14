/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

   
    int getDecimalValue(ListNode* head) {
        int value = 0;
        for (auto curr = head; curr != nullptr; curr = curr->next) {
            value = curr->val ? value * 2 + 1 : value * 2;
        }
        return value;
    }
};