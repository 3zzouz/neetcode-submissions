class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l<r-1:
            mil = int((l+r)/2)
            if target < matrix[mil][0]:
                r = mil
            elif target > matrix[mil][0]:
                l = mil
            else:
                return True
        array=[]
        if target >= matrix[r][0]:
            array = matrix[r]
        elif target <= matrix[l][-1] :
            array = matrix[l]
        else :
            return False
        l = 0
        r = len(array) - 1
        print(r)
        while l<r-1:
            mil = int((l+r)/2)
            if target < array[mil]:
                r = mil
            elif target > array[mil]:
                l = mil
            else:
                return True
        print(l,r)
        return array[l] == target or array[r] == target
