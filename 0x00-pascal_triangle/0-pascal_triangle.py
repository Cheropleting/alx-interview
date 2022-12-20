def pascal_triangle(n):
    triangle = []
    
    if n <= 0:
        return triangle
    
    triangle.append([1])
    
    for i in range(1, n):
        prev_row = triangle[i-1]
        new_row = [0] + prev_row + [0]
        triangle.append([new_row[j] + new_row[j+1] for j in range(len(prev_row))])
    
    return triangle
