class Solution(object):
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

        You must implement a solution with a linear runtime complexity and use only constant extra space.
        """
        num_set = set(nums)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n3 = nums1 + nums2
        n3.sort()
        mid = len(n3) // 2
        if len(n3) % 2:
            return n3[mid]
        return sum(n3[mid-1:mid+1]) / 2


a = Solution()
print(a.findMedianSortedArrays([1, 2, 4], [3, 4, 6]))
