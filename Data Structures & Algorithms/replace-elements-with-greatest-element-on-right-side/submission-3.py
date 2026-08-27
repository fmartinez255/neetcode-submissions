class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # given an arr of any int
        # replace every elem with greatest elem among the elements to right
        # replace last elem with -1

        # brute force:
        #  2 for loops
        #  for i in len(arr)
        #   if i != len(arr):
        #    get greatest elem from right
        #    greatest = 0
        #    for j in range(i,len(arr)):
        #      greatest = max(greatest, arr[j])
        #    arr[i] = greatest
        #   else return arr[i] = -1
        #
        # not efficient (O(n^2))

        # more efficient (O(n))?
        #
        # for each index of arr, find max of all elements (max(arr))
        # slide index over by one and repeat

        for k, v in enumerate(arr):
            idx = k+1
            if idx == len(arr):
                arr[k] = -1
            else:
                arr[k] = max(arr[idx:])
        return arr