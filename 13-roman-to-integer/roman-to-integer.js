/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    const romanCharToInt = (char) => {
        switch (char) {
            case 'M':
                return 1000;
            case 'D':
                return 500;
            case 'C':
                return 100;
            case 'L':
                return 50;
            case 'X':
                return 10;
            case 'V':
                return 5;
            case 'I':
                return 1;
            default:
                return -1;
        }
    }
    var inte = 0;
    for (let i = 0; i < s.length; i++) {
        let num = romanCharToInt(s.charAt(i));
        if (i < s.length) {
            let nextNum = romanCharToInt(s.charAt(i + 1));
            if (nextNum > num) {
                inte -= num;
            } else {
                inte += num;
            }
        }
    }
    return inte;
};