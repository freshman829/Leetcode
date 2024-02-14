/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const result = new Array(nums.length).fill(0);
    let positiveStep = 0;
    let negativeStep = 1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= 0) {
            result[positiveStep] = nums[i];
            positiveStep += 2;
        } else {
            result[negativeStep] = nums[i];
            negativeStep += 2;
        }
    }
    return result;
    
};