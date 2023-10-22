import math

a = math.isclose(1.1111111, 1.11111110, abs_tol=0.0001)
print(a)

b = math.isclose(333333, 333334, rel_tol=0.01)
print(b)
