class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] = triangle[row][col] + min(triangle[row + 1][col], triangle[row + 1][col + 1])

        print(triangle)
        return triangle[0][0]