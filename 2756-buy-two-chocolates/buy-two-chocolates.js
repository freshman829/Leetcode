/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
    prices.sort((a, b) => a - b);
    let sum = prices[0];
    if (sum > money) return money;
    if (sum + prices[1] > money) return money;
    return money - prices[0] - prices[1];
};