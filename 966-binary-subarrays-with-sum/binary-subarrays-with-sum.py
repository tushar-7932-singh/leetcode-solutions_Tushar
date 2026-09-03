class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        s = ans = 0

        for x in nums:
            s += x
            ans += count.get(s - goal, 0)
            count[s] = count.get(s, 0) + 1

        return ans