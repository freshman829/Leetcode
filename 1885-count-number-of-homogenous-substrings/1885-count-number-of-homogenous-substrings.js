/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function (s) {
    const MOD = 1000000007;
    let count = 0;
    let currentChar = '';
    let currentLength = 0;

    for (const char of s) {
        if (char === currentChar) {
            currentLength++;
        } else {
            currentChar = char;
            currentLength = 1;
        }

        count = (count + currentLength) % MOD;
    }

    return count;
};