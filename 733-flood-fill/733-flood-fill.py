class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = dict()
        def isvalid(r,c):
            if r<len(image) and r>-1 and c>-1 and c<len(image[0]):
                return True
            return False
        
        def fill(r,c,color):
            if not isvalid(r,c) or (r,c) in visited:
                return 
            if image[r][c] == color: 
                image[r][c]  = newColor
                visited[(r,c)] = True

                fill(r,c-1,color)
                fill(r,c+1,color)
                fill(r+1,c,color)
                fill(r-1,c,color)
        fill(sr,sc,image[sr][sc])
        return image
