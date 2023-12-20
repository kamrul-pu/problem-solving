def merge(nums: list[int], low: int, mid: int, high: int) -> None:
    temp: list[int] = []
    left: int = low
    right: int = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]


def merge_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        mid: int = (low + high) // 2
        merge_sort(nums=nums, low=low, high=mid)
        merge_sort(nums=nums, low=mid + 1, high=high)
        merge(nums=nums, low=low, mid=mid, high=high)


def partition(nums: list[int], low: int, high: int) -> int:
    pivot: int = nums[low]
    i: int = low
    j: int = high
    while i < j:
        while i < high and nums[i] <= pivot:
            i += 1
        while j > low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        p_i: int = partition(nums=nums, low=low, high=high)
        quick_sort(nums=nums, low=low, high=p_i - 1)
        quick_sort(nums=nums, low=p_i + 1, high=high)


if __name__ == "__main__":
    nums: list[int] = [19, 3, 78, 3, 2, 5, 9, -5]
    print(nums)
    # merge_sort(nums=nums, low=0, high=len(nums) - 1)
    quick_sort(nums=nums, low=0, high=len(nums) - 1)
    print(nums)
