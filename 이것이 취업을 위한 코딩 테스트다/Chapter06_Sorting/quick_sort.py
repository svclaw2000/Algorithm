array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    """
    :param array: 정렬할 리스트
    :param start: 시작 원소 idx
    :param end:   마지막 원소 idx (슬라이스 아님)
    :return:
    """
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # array[left] > array[pivot]인 left 의 위치 찾을 때까지.
        # left > end 면 리스트 넘어감.
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # array[right] < array[pivot]인 right 의 위치 찾을 때까지.
        # right == start 면 피벗.
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # pivot : 기준, right : 더 작은 원소, left : 더 큰 원소
        # 작은 원소가 왼쪽에 있을 때, 즉, pivot을 기준으로 좌우가 정렬되었을 때
        if right < left:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    # pivot이 right 위치에 있음
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)