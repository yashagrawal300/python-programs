'''Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.'''



class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        y = []
        for i in range(len(A)):
            y.append(A[i]**2)
        y.sort()
        return y
