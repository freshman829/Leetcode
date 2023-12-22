/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let result = 0;
    for (let i = 1; i < s.length; i++) {
        let sum = getCount(s.slice(0, i), true) + getCount(s.slice(i), false);
        if (sum > result)
            result = sum;
    }
    return result;
};
    
const getCount = (string, isLeft) => {
    let filtered = [];
    if (isLeft) {
        filtered = string.split("").filter((char) => char === "0");
    } else {
        filtered = string.split("").filter((char) => char === "1");
    }
    return filtered.length;
}