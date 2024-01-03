# To find the maximum number of points that lie on the same line in a given set of points using a hash table
# Input : points[] = {-1, 1}, {0, 0}, {1, 1}, 
#                     {2, 2}, {3, 3}, {3, 4} 
# Output : 4
# Then maximum number of point which lie on same
# line are 4, those point are {0, 0}, {1, 1}, {2, 2},
# {3, 3} hash method


# Defaultdict is a container like dictionaries present in the module collections.
# Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
# The functionality of both dictionaries and defaultdict are almost same except for the fact 
# that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

# Syntax: defaultdict(default_factory)
# Parameters:  

# default_factory: A function returning the default value for the dictionary defined. 
# If this argument is absent then the dictionary raises a KeyError.

# Example
# from collections import defaultdict 
  
  
# # Function to return a default 
# # values for keys that is not 
# # present 
# def def_value(): 
#     return "Not Present"
      
# # Defining the dict 
# d = defaultdict(def_value) 
# d["a"] = 1
# d["b"] = 2
  
# print(d["a"]) 1
# print(d["b"]) 2
# print(d["c"]) Not present


from collections import defaultdict

def MaxPoints(points):
    if not points:
        return 0
    
    max_points = 1
    for i in range(len(points)):
        slope_count = defaultdict(int)
        same_points = 0
        for j in range(i+1, len(points)):
            x_diff = points[j][0] - points[i][0]
            y_diff = points[j][1] - points[i][1]
            
            if x_diff == 0 and y_diff == 0:
                same_points += 1
                continue
            
            gcd = findGCD(x_diff, y_diff)
            x_diff //= gcd
            y_diff //= gcd
            
            slope_count[(x_diff, y_diff)] += 1
        
        current_max = same_points + 1 if slope_count else 1
        for val in slope_count.values():
            current_max = max(current_max, val + same_points + 1)
        max_points = max(max_points, current_max)
    return max_points
            


def findGCD(a,b):
    while b:
        a,b = b, a%b
    return a

points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
print(f"Maximum number of points lying on the same line: { MaxPoints(points)}.") # 4

# Output
# maxPointsOnLine is the main function that takes a list of points as input and 
# returns the maximum number of points that lie on the same line.

# It initializes max_points to 1 and then iterates through each point.

# Within the loop, it creates a defaultdict called slope_count to store 
# the count of slopes between the current point and other points.

# It also keeps track of the count of points that are identical to the 
# current point using the variable same_points.

# The nested loop calculates the slope between the current point and 
# all other points and stores the slope counts in the slope_count dictionary.

# Additionally, it identifies and counts points that are the same as the current point.

# findGCD calculates the greatest common divisor (GCD) of two numbers.

# Finally, the code computes the current_max based on the counts of points with the same slope, 
# considering points that are identical, and updates max_points with the maximum count found.

            