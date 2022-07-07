class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1
        while top < down:
            mid = (top + down) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                # top will hold the corerct row's range
                top = mid
                break;
            elif target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
        # this new array holds the range where we need to search
        arr = matrix[top]
        left, right = 0, len(matrix[top]) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        