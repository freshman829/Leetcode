/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    let pointXs = [];
    var max = 0;
    for (let i = 0; i < points.length; i++) {
        pointXs.push(points[i][0]);
    }
    pointXs.sort((a, b) => a - b);
    for (let i = 0; i < pointXs.length - 1; i++) {
        if (pointXs[i + 1] - pointXs[i] > max)
            max = pointXs[i + 1] - pointXs[i];
    }
    return max
};