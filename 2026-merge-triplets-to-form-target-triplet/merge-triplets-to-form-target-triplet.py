class Solution:
    def mergeTriplets(self, triplets, target):
        a = [0, 0, 0]

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a[0] = max(a[0], x)
                a[1] = max(a[1], y)
                a[2] = max(a[2], z)

        return a == target   