/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    let leftRemove = 0;
    let rightRemove = 0;

    // Find minimum number of '(' and ')' to remove
    for (let ch of s) {
        if (ch === '(') {
            leftRemove++;
        } else if (ch === ')') {
            if (leftRemove > 0) {
                leftRemove--;
            } else {
                rightRemove++;
            }
        }
    }

    let result = new Set();

    function dfs(index, left, right, balance, current) {
        // If we reached the end
        if (index === s.length) {
            if (left === 0 && right === 0 && balance === 0) {
                result.add(current);
            }
            return;
        }

        let ch = s[index];

        // Option 1: Remove current character
        if (ch === '(' && left > 0) {
            dfs(index + 1, left - 1, right, balance, current);
        }

        if (ch === ')' && right > 0) {
            dfs(index + 1, left, right - 1, balance, current);
        }

        // Option 2: Keep current character
        if (ch !== '(' && ch !== ')') {
            dfs(index + 1, left, right, balance, current + ch);
        } 
        else if (ch === '(') {
            dfs(index + 1, left, right, balance + 1, current + ch);
        } 
        else if (ch === ')' && balance > 0) {
            dfs(index + 1, left, right, balance - 1, current + ch);
        }
    }

    dfs(0, leftRemove, rightRemove, 0, "");

    return [...result];
};