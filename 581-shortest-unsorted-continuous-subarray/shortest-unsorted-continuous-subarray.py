class Solution:
    def findUnsortedSubarray(self, nums):
        s = sorted(nums)
        l = 0
        r = len(nums) - 1

        while l < len(nums) and nums[l] == s[l]:
            l += 1

        while r >= 0 and nums[r] == s[r]:
            r -= 1

        return max(0, r - l + 1)
        