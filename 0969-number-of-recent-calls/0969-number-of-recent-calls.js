
var RecentCounter = function() {
    this.requests = [];
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.requests.push(t);
    // Remove requests that are outside the time frame [t - 3000, t]
    while (this.requests[0] < t - 3000) {
      this.requests.shift();
    }
    // Return the number of requests within the time frame
    return this.requests.length;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */