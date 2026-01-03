import math
def get_angle(x,y):
    return math.atan2(y,x)

def sort_close_to_y_axis(points):
    return sorted(points, key=lambda p: (abs(p[0]), get_angle(p[0],p[1])))

def closest_point_to_origin(points):
    return min(points, key=lambda p: (abs(p[0]) + abs(p[1]), get_angle(p[0],p[1])))

def get_quadrant(point):
    x, y = point
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

def group_by_quadrant(points):
    groups = {}
    for point in points:
        quadrant = get_quadrant(point)
        if quadrant not in groups:
            groups[quadrant] = set()
        groups[quadrant].add(point)
    return groups


def process_points(points:set, task:str):
    """Process the ponts according to the given task.

    Args:
        points (set[tuple[int,int]]) - Set of points in 
            cartesian corrdinates as (x,y) tuples
        task (str) - String with one of the below values.
            - 'sort_close_to_y_axis'
            - 'closest_point_to_origin'
            - 'group_by_quadrant'

    Returns:
        The output of the corresponding task.

    """
    
    
    if task == "sort_close_to_y_axis":
        return sort_close_to_y_axis(points)
    elif task == "closest_point_to_origin":
        return closest_point_to_origin(points)
    elif task == "group_by_quadrant":
        return group_by_quadrant(points)


# #Another Method:
# import math
# def get_angle(x,y):
#     return math.atan2(y,x)


# def process_points(points:set, task:str):
#     """Process the ponts according to the given task.

#     Args:
#         points (set[tuple[int,int]]) - Set of points in 
#             cartesian corrdinates as (x,y) tuples
#         task (str) - String with one of the below values.
#             - 'sort_close_to_y_axis'
#             - 'closest_point_to_origin'
#             - 'group_by_quadrant'

#     Returns:
#         The output of the corresponding task.

#     """
#     if task=="sort_close_to_y_axis":
#         l=list(points)
#         for i in range(len(l)):
#             for j in range(i+1,len(l)):
#                 x1,y1=l[i]
#                 x2,y2=l[j]
#                 if abs(x1)>abs(x2):
#                     l[i],l[j]=l[j],l[i]
#                 if abs(x1)==abs(x2):
#                     a1=get_angle(x1,y1)
#                     a2=get_angle(x2,y2)
                    
#                     if a1>a2:
#                         l[i],l[j]=l[j],l[i]
#         return l
#     if task == "closest_point_to_origin":
#         l=list(points)
#         xmin=1000
#         ymin=1000
#         for i in range(len(l)):
#             x1,y1=l[i]
#             if abs(xmin)+abs(ymin) > abs(x1)+abs(y1):
#                 xmin=x1
#                 ymin=y1
                
#             if abs(xmin)+abs(ymin) == abs(x1)+abs(y1):
#                     a1=get_angle(xmin,ymin)
#                     a2=get_angle(x1,y1)
                    
#                     if a1>a2:
#                         xmin=x1
#                         ymin=y1
                        
#         return (xmin,ymin)
    
#     if task == "group_by_quadrant":
#         d={}
#         set1=set()
#         set2=set()
#         set3=set()
#         set4=set()
#         l=list(points)
#         for i in range(len(l)):
#             x1,y1=l[i]
#             if x1>0:
#                 if y1>0:
#                     set1.add(l[i])
#                 else:
#                     set4.add(l[i])
#             else:
#                 if y1>0:
#                     set2.add(l[i])
#                 else:
#                     set3.add(l[i])
#         if len(set1)!=0:
#             d[1]=set1
#         if len(set2)!=0:
#             d[2]=set2
#         if len(set3)!=0:
#             d[3]=set3
#         if len(set4)!=0:
#             d[4]=set4
            
#         return (d)
        
#  Cartesian Points Processing
# Given a set of tuples of ints representing points in Cartesian coordinates, write a function that performs the following tasks:

# sort_close_to_y_axis: Returns a sorted list of the points based on the absolute value of their x-coordinate (distance from the y-axis). The point with the lower angle in polar coordinates comes first in case of ties.
# closest_point_to_origin: Find the closest point to the origin (0,0) based on the Manhattan distance. If there are multiple points at the same distance, return the one with the lower angle in polar coordinates.
# group_by_quadrant: Return a dictionary where the keys are quadrant numbers (1, 2, 3, 4) and the values are sets of points in those quadrants. Do not include keys for quadrants with no points.
# Note the angle is computed using math.atan2(y,x) where x and y are the cartesian coordinates. math.atan2 returns the angle in the range of -pi to pi. You can use the get_angle function from the template.

# Assume no points are on the axes or origin and the coordinates are integers.

# Hint: sorted and min functions can be used with the key argument to make the code simpler.

# Definitions:

# Manhattan distance between two points (x_1, y_1) and (x_2, y_2) is |x_1 - x_2| + |y_1 - y_2|.

# Example

# points = {
#     (2, 5), (-2, 6), (-2, 7), (-1, 3),
#     (-3, -4), (4, -6), (0, 7)
# }
# task = "sort_close_to_y_axis"
# output = [
#     (0, 7), (-1, 3), (2, 5), (-2, 7),
#     (-2, 6), (-3, -4), (4, -6)
# ]
# is_equal(
#     process_points(points, task),
#     output
# )       
                        
        
                        
                    
            
            
            
    

    
