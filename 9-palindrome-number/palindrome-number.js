/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let ordered = parseInt(x.toString().split('').reverse().join(""));
    return ordered === x;
};