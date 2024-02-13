/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function (head) {
    // Find the length of the linked list
    let length = 0;
    let current = head;
    while (current) {
        length++;
        current = current.next;
    }

    // Reverse the second half of the linked list
    let mid = Math.floor(length / 2);
    let secondHalf = head;

    for (let i = 0; i < mid; i++) {
        secondHalf = secondHalf.next;
    }

    secondHalf = reverseLinkedList(secondHalf);

    // Find the maximum twin sum
    let maxSum = 0;
    let pointer1 = head;
    let pointer2 = secondHalf;

    for (let i = 0; i < mid; i++) {
        maxSum = Math.max(maxSum, pointer1.val + pointer2.val);
        pointer1 = pointer1.next;
        pointer2 = pointer2.next;
    }

    return maxSum;
}

const reverseLinkedList = (head) => {
    let prev = null;
    let current = head;

    while (current) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};
