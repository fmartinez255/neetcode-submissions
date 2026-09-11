# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs

        self.msort(pairs, 0, len(pairs)-1)

        return pairs

    def merge(self, pairs: List[Pair], start: int, middle: int, end: int):
        # Copy the sorted left & right halfs to temp arrays
        L = pairs[start: middle+1]
        R = pairs[middle+1: end+1]

        i = 0 # index for L
        j = 0 # index for R
        k = start # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

    def msort(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs

        middle = (start + end) // 2

        self.msort(pairs, start, middle)
        self.msort(pairs, middle+1, end)

        self.merge(pairs, start, middle, end)
