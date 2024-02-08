/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) !== ')' && s.charAt(i) !== '}' && s.charAt(i) !== ']') {
            stack.push(s.charAt(i));
        } else {
            if (stack.length === 0) return false;
            if (s.charAt(i) === ')' && stack[stack.length - 1] === '('
                || s.charAt(i) === '}' && stack[stack.length - 1] === '{'
                || s.charAt(i) === ']' && stack[stack.length - 1] === '['
            ) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return stack.length ? false : true;
};