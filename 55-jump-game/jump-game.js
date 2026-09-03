 /**
  * @param {number[]} nums
  * @return {boolean}
  */
var canJump = function(nums) {
    let maxReach = 0;

    for (let i = 0; i < nums.length; i++) {
        // If current position is unreachable
        if (i > maxReach) {
            return false;
        }

        maxReach = Math.max(maxReach, i + nums[i]);

        // We can already reach the last index
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }

    return true;
};