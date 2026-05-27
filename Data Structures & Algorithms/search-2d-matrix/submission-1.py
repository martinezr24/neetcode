class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l_r, r_r = 0, n - 1

        row = -1
        while l_r <= r_r:
            m_r = (l_r + r_r) // 2
            if target >= matrix[m_r][0] and target <= matrix[m_r][-1]:
                row = m_r
                break
            elif target > matrix[m_r][-1]:
                l_r = m_r + 1
            else:
                r_r = m_r - 1
        if row == -1:
            return False
        
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False