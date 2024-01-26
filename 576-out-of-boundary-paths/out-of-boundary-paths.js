/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function(m, n, maxMove, startRow, startColumn) {
    const MOD = 1000000007;
    let dp = new Array(m).fill(0).map(() => new Array(n).fill(0));
    dp[startRow][startColumn] = 1;
    let count = 0;
    
    // Define directions
    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    
    for (let move = 1; move <= maxMove; move++) {
        let temp = new Array(m).fill(0).map(() => new Array(n).fill(0));
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                for (const [dx, dy] of dirs) {
                    let x = i + dx;
                    let y = j + dy;
                    if (x < 0 || x >= m || y < 0 || y >= n) {
                        count = (count + dp[i][j]) % MOD;
                    } else {
                        temp[x][y] = (temp[x][y] + dp[i][j]) % MOD;
                    }
                }
            }
        }
        dp = temp;
    }
    
    return count;
};