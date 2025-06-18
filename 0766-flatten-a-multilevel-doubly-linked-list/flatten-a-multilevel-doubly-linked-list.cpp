/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return nullptr;

        if (head->child) {
            auto curr = head->child;
            head->child = nullptr;
            auto next_node = flatten(curr);

            // get tail
            auto tail = next_node;
            while (tail->next != nullptr) {
                tail = tail->next;
            }

            auto seq = head->next;
            if (seq) {
                seq->prev = tail;
            }
            tail->next = seq;

            head->next = next_node;
            next_node->prev = head;
        }

        flatten(head->next);

        return head;
    }
};