/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    nums.sort((a, b) => a - b); // Sort the array in ascending order

    const result = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i === 0 || (i > 0 && nums[i] !== nums[i - 1])) { // Skip duplicate elements
            let left = i + 1;
            let right = nums.length - 1;
            const target = -nums[i];

            while (left < right) {
                const sum = nums[left] + nums[right];

                if (sum === target) {
                    result.push([nums[i], nums[left], nums[right]]);
                    while (left < right && nums[left] === nums[left + 1]) left++; // Skip duplicate elements
                    while (left < right && nums[right] === nums[right - 1]) right--; // Skip duplicate elements
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return result;
};