def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    find the median of two arrays
    """
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty")

    # Merge the two arrays
    merged = sorted(nums1 + nums2)
    total = len(merged)

    if total % 2 == 1:  # if the total number of elements is odd
        return float(merged[total // 2])  # then return the middle element

    # If the total number of element is even calculate
    # the average of two middle elements as the median
    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]

    return (float(middle1) + float(middle2)) / 2.0


nums1 = [1, 2]
nums2 = [3, 4]

print(find_median_sorted_arrays(nums1, nums2))
