/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGood = function (nums) {
    if (!nums.length) return true;
    let maxVal = nums.sort((a, b) => b - a)[0];
    if (nums.length !== maxVal + 1) {
        return false;
    }
    if (nums.length > 2 && nums[0] !== nums[1]) return false;
    for (let i = 1; i <= maxVal; i++) {
        if (nums.findIndex((num) => num === i) < 0) return false;
    }
    return true;

};