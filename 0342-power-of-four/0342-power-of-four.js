/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if (n === 1)
        return true;
    else if (n < 1)
        return false;
    else {
        let temp = n;
        while (temp > 1) {
            if (temp % 4 > 0) return false;
            temp = temp / 4;
        }
        return true;
    }
};