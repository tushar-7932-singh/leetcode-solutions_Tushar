var myAtoi = function(s) {
    s = s.trim();

    let sign = 1, i = 0, num = 0;

    if (s[i] === '-' || s[i] === '+') {
        if (s[i] === '-') sign = -1;
        i++;
    }

    while (i < s.length && s[i] >= '0' && s[i] <= '9') {
        num = num * 10 + (s[i] - '0');
        i++;
    }

    num *= sign;

    return Math.max(-2147483648, Math.min(2147483647, num));
};