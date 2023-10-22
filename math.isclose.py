import math

"""
abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero.
"""
a = math.isclose(1.1111111, 1.11111110, abs_tol=0.0001)
print(a)


"""
rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, 
relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, 
pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values are 
the same within about 9 decimal digits. rel_tol must be greater than zero.
"""
b = math.isclose(333333, 333334, rel_tol=0.01)
print(b)
