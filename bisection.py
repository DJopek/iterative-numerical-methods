import math

# the function
def f(x):
    # return 2**x - 4**(-x) + 1
    return math.log(x) - x**(-2)

# bounds of the interval
a = float(input("Enter the first bound of the interval: "))
b = float(input("Enter the second bound of the interval: "))

# tolerance level
tol = 1e-6

# bisection method iteratively
for i in range(100):

    # midpoint of a and b
    c = (a+b)/2

    # update a or b depending on the sign of f(a)*f(c) or f(b)*f(c)
    if f(a)*f(c) < 0:
        a = a
    elif f(b)*f(c) < 0:
        a = b

    b = c

    print(f"Iteration {i+1}: Root: {c:.6f}")

    if abs(f(c)) < tol:
        break