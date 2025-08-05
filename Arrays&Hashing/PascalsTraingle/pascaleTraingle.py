from typing import List
# NCR for finding specific value in triangle
def valueOfNcr(n:int , r:int)-> int:
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res 

print(valueOfNcr(5,2))    

# for generating full triangle
def generateTriangle(numRows: int) -> List[List[int]]:
    triangles = []
    
    for i in range(numRows):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = triangles[i - 1][j - 1] + triangles[i - 1][j]
        
        triangles.append(row)
    
    return triangles


print(generateTriangle(3))