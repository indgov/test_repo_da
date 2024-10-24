import math

# Function to find the roots of the quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if discriminant is positive, zero or negative
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant) ** 2) / (2 * a)
        return f"The equation has two real and distinct roots: {root1} and {root2}"
    
    elif discriminant == 0:
        # One real root (double root)
        root = -b / (2 * a)
        return f"The equation has one real root: {root}"
    
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

aa = find_roots(-6, 36, -59)
o = 1