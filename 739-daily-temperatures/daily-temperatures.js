/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = [];
    const answer = new Array(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length; i++) {
        while (stack.length && temperatures[i] > temperatures[stack[stack.length - 1]]) {
            const index = stack.pop();
            answer[index] = i - index;
        }
        stack.push(i);
    }

    return answer;
};