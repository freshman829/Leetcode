/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const anagrams = {};

    for (const word of strs) {
        const sortedWord = word.split('').sort().join('');

        if (!(sortedWord in anagrams)) {
            anagrams[sortedWord] = [word];
        } else {
            anagrams[sortedWord].push(word);
        }
    }

    return Object.values(anagrams);
};