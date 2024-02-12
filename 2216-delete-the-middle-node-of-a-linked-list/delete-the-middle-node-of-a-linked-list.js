/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (!head || !head.next) {
        // No middle node to delete
        return null;
    }

    // Step 1: Find the length of the linked list
    let length = 0;
    let current = head;
    while (current) {
        length++;
        current = current.next;
    }

    // Step 2: Identify the middle node
    const middleIndex = Math.floor(length / 2);
    let prev = null;
    current = head;

    for (let i = 0; i < middleIndex; i++) {
        prev = current;
        current = current.next;
    }

    // Step 3: Update pointers to skip the middle node
    if (prev) {
        prev.next = current.next;
    } else {
        // If the middle node is the head, update the head
        head = head.next;
    }

    return head;
};