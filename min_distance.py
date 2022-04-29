# Time complexity: M * log(N) 
# Iterate through the shorter list and binary search the longer list to find smallest distance
def minDistance(list1, list2):
    min_dist = float("inf")
    
    shorter_list = list1 if len(list1) <= len(list2) else list2
    longer_list = list1 if len(list1) > len(list2) else list2

    def findMinDistance(num: int, list2: typing.List[str]) -> None:
            nonlocal min_dist
            mid = len(list2) // 2
            if len(list2) == 1:
                min_dist = min(min_dist, abs(list2[0] - num))
            elif num >= list2[mid]:
                findMinDistance(num, list2[mid + 1:])
            elif num < list2[mid]:
                findMinDistance(num, list2[:mid])

    for i in shorter_list:
        findMinDistance(i, longer_list)
    
    return min_dist
