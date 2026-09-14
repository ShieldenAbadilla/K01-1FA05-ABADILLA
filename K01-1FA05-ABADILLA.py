import math

# Calculate the Euclidean Distance Formula between two 2D points.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"{distance:.2f}")

# Reflection and Evaluation
# Using a library is more practical because it provides functions that make calculations easier and faster. 
# In this activity, math.sqrt() and math.pow() helped me calculate the distance without having to create the calculations from scratch. 
# Without these functions, the program would be more difficult because I would have to find another way to calculate square roots and powers.
