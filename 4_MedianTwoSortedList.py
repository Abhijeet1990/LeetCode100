
def findMedianSortedArrays(nums1, nums2):
    # one heck of a code
    total = len(nums1) + len(nums2)
    half = total // 2

    # analyse things in a shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # now nums1 is the short list
    l, r = 0, len(nums1) - 1

    while True:
        nums1_mid = (l + r) // 2

        # get a tentative mid for the nums2
        nums2_mid = half - nums1_mid - 2

        # left and right at every boundaries for both the list are computed for comparison of nums1 left with nums2 right and vice-versa
        nums1_l = nums1[nums1_mid] if nums1_mid >= 0 else float('-inf')
        nums1_r = nums1[nums1_mid + 1] if (nums1_mid + 1) < len(nums1) else float('inf')
        nums2_l = nums2[nums2_mid] if nums2_mid >= 0 else float('-inf')
        nums2_r = nums2[nums2_mid + 1] if (nums2_mid + 1) < len(nums2) else float('inf')

        # comparison
        if nums1_l <= nums2_r and nums2_l <= nums1_r:
            # if total is odd
            if total % 2:
                return min(nums1_r, nums2_r)
            else:
                return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2

        elif nums1_l > nums2_r:
            r = nums1_mid - 1
        else:
            l = nums1_mid + 1


A = [3,6,8,9,12,89]
B = [5,8,12,13,56,88,92]
print('Median of two sorted array : ',findMedianSortedArrays(A,B))