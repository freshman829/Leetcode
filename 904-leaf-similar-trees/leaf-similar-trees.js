/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function (root1, root2) {
    const getLeafNodes = (root, leaves) => {
        if (!root) {
            return;
        }

        if (!root.left && !root.right) {
            leaves.push(root.val);
        }

        getLeafNodes(root.left, leaves);
        getLeafNodes(root.right, leaves);
    }

    const leaves1 = [];
    const leaves2 = [];

    getLeafNodes(root1, leaves1);
    getLeafNodes(root2, leaves2);

    // Check if the leaf value sequences are the same
    return leaves1.join() === leaves2.join();
};