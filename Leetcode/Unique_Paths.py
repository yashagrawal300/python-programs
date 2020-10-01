class Solution(object):
    def uniquePaths(self, x, y):
        """
        :data type of x: int
        :data type y: int
        :return type: int
        """
        #### DP solution ####
        
        # Edge Cases
        if x <= 0 or y <= 0:
            return 0
        if x == 1 or y == 1:
            return 1
        
        # build an empty matrix
        matrix = [[1 for j in range(y)]for i in range(x)]
        print(matrix)
        
        # Record steps for each cell using DP (Except the 1st Row and the 1st Column, since there is only one way to get the cells in these places..)
        for i in range(1,x):
            for j in range(1,y):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]