import math

"""
Newton's method that returns the root and the number of iterations
f - function
df - derivative of the function
x0 - numerical value (root estimate)
tol - the range of f(x) that is tolerated, which we want to fit to
max_iter - maximum number of iterations
"""

def newtons_method(f, df, x0, tol=1e-6, max_iter=100):

    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i
        dfx = df(x)
        if dfx == 0:
            break
        x -= fx / dfx
        print(f"Iterácia {i+1}: {x:.6f}")

    return x, i+1

# the function
def f(x):
    # return 2**x - 4**(-x) + 1
    return math.log(x) - x**(-2)

# derivative of the function
def df(x):
    # return 2**x * math.log(2) + 4**(-x) * math.log(4)
    return 1/x + 2*x**(-3)

root, iterations = newtons_method(f, df, x0=1)
print(f"Root : {root:.6f}")
print(f"Iteration : {iterations}")