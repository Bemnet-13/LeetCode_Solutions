class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # [1,4,7,0,0,0] [2,5,6]
        # [1,2,7,0,0,0] [4,5,6]
        # [1,2,4,0,0,0] [7,5,6]
        # [1,2,4,7,0,0] [7,5,6]
        # [1,2,4,7,5,0] [7,5,6]
        # [1,2,4,5,7,0] [7,5,6]
        # [1,2,4,5,7,6] [7,5,6]
        # [1,2,4,5,6,7] [7,5,6]

        l = len(nums1)
        r = len(nums2)
        i = 0
        j = 0

        while i < l and j < r:
            if nums1[i] <= nums2[j] and i < m:
                i += 1
                if i == m:
                    nums2.sort()
            elif nums1[i] <= nums2[j] and i >= m:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                # i += 1
                
        print(nums1)
trial = Solution()
trial.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3)