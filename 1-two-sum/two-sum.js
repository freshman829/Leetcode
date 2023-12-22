/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  
    for (let i = 0; i < nums.length; i++) {
        let sub = target - nums[i];
        let idx = nums.findIndex((num, index) => num === sub && index !== i);
        if (idx > 0) return [i, idx];
    }
    return null;
};