/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    if (num <= 0 || num > 3999) {
        return "Invalid input. Please enter a number between 1 and 3999.";
    }

    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let result = "";

    for (let i = 0; i < values.length; i++) {
        while (num >= values[i]) {
            result += numerals[i];
            num -= values[i];
        }
    }

    return result;
};