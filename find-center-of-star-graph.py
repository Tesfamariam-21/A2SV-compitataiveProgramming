class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        for i in range(len(edges)-1):
            if edges[i][0] in edges[i+1]:
                return edges[i][0]
            elif edges[i][1] in edges[i+1]:
                return edges[i][1]