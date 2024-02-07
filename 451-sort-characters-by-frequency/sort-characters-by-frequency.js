/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function (s) {
    const charFrequency = {};

    for (const char of s) {
        charFrequency[char] = (charFrequency[char] || 0) + 1;
    }

    const sortedChars = Object.keys(charFrequency).sort((a, b) => charFrequency[b] - charFrequency[a]);

    let result = '';
    for (const char of sortedChars) {
        result += char.repeat(charFrequency[char]);
    }

    return result;
};