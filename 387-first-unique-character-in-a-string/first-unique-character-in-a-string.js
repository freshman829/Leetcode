/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const uniqueArr = [...new Set(s.split(''))];
    for (let i = 0; i < uniqueArr.length; i++) {
        let char = uniqueArr[i];
        let firstIndex = s.indexOf(char);
        let lastIndex = s.lastIndexOf(char);
        if (firstIndex === lastIndex) {
            return firstIndex;
        }
    }
    return -1;
};