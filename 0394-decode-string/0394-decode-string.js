/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    const stack = [];
    let currentNumber = 0;
    let currentString = '';

    for (let char of s) {
        if (char === '[') {
            stack.push(currentString);
            stack.push(currentNumber);
            currentString = '';
            currentNumber = 0;
        } else if (char === ']') {
            const prevNumber = stack.pop();
            const prevString = stack.pop();
            currentString = prevString + currentString.repeat(prevNumber);
        } else if (/[0-9]/.test(char)) {
            currentNumber = currentNumber * 10 + parseInt(char);
        } else {
            currentString += char;
        }
    }

    return currentString;
};