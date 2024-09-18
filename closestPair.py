def distance_two_points(a, b):
    return (((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)) ** 0.5

def closest_pair(points):
    if len(points) < 2:
        return 'Not enought points.'
    
    distance_min = float("inf")
    first_point, second_point = None, None 
    
    for i in range(len(points) - 1):  
        for j in range(i + 1, len(points)):
            distance = distance_two_points(points[i], points[j])
            if distance < distance_min:
                distance_min = distance
                first_point = points[i]
                second_point = points[j]
    
    return first_point, second_point, distance_min

points = [[0,0],[2,2],[3,3]]
print(closest_pair(points))
