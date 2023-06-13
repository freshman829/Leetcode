/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    var cnt = 0;
    for (let i = 0; i < grid.length; i++) {
        let row = grid[i];
        for (let j = 0; j < grid.length; j++) {
            let col = [];
            for (let k = 0; k < grid.length; k++)
                col.push(grid[k][j]);
            if (equalArray(row, col)) {
                cnt++;
            }
        }
    }
    return cnt;
};

/**
 * @param {number[]} row
 * @param {number[]} col
 * @return {boolean}
 */
var equalArray = (row, col) => {
    if (row.length != col.length)
        return false;
    for (let i = 0; i < row.length; i++) 
        if (row[i] != col[i])
            return false;
    return true;
        
}