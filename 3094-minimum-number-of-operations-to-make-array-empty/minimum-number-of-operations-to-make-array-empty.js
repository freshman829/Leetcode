/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const counts = {}; 
    for (const num of nums) {
    counts[num] = (counts[num] || 0) + 1;
    }

    for (const count of Object.values(counts)) {
    if (count === 1 || getOpCnt(count) === -1 || getOpCnt(count) === Infinity) return -1;
    }

    const mostFreqNum = Object.keys(counts).reduce((maxNum, num) => {
    return counts[num] > counts[maxNum] ? num : maxNum;
    }, 0);

    let totalOpCnt = 0;
    for (const num in counts) {
    if (num !== mostFreqNum) {
      const count = counts[num];
      const minOps = getOpCnt(count); // Or use a lookup table
      if (minOps === Infinity || minOps === -1) return -1;
      totalOpCnt += minOps;
    }
    }

    return totalOpCnt;
};

var getOpCnt = (len) => {
    if (len % 3 === 0) return len / 3;
    if (len === 2) return 1;
    for (let i = Math.floor(len / 3); i >= 0; i--) {
        let free = len - i * 3;
        if (free % 2 == 0) {
            return i + free / 2;
        }
    }
    return -1;
}