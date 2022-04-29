def minDistance(list1, list2):
    min_dist = float("inf")
    def findMinDistance(num: int, list2: typing.List[str]) -> None:
            nonlocal min_dist
            mid = len(list2) // 2
            if len(list2) == 1:
                min_dist = min(min_dist, abs(list2[0] - num))
            elif num >= list2[mid]:
                findMinDistance(num, list2[mid + 1:])
            elif num < list2[mid]:
                findMinDistance(num, list2[:mid])

    for i in list1:
        findMinDistance(i, list2)
    
    return min_dist