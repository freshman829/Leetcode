/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kInversePairs = function(n, k) {
   const MOD = 1000000007;
    let dp = new Array(n + 1).fill(0).map(() => new Array(k + 1).fill(0));
    dp[1][0] = 1;

    for (let i = 2; i <= n; i++) {
        let prefixSum = new Array(k + 1).fill(0);
        prefixSum[0] = dp[i - 1][0];
        for (let j = 1; j <= k; j++) {
            prefixSum[j] = (prefixSum[j - 1] + dp[i - 1][j]) % MOD;
        }
        for (let j = 0; j <= k; j++) {
            let val = (prefixSum[j] - (j - i >= 0 ? prefixSum[j - i] : 0) + MOD) % MOD;
            dp[i][j] = val
        }
    }

    return dp[n][k];
};