/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    function isPalindrome(str) {
        return str === str.split('').reverse().join('');
    }

    for (const word of words) {
        if (isPalindrome(word)) {
            return word;
        }
    }

    return "";
};