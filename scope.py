x = 6


def f():
    print("Within f: x =", x)
    x = 12
    print("Within f: x =", x)


print("Before f: x =", x)
f()
print("After f: x =", x)

# Before f: x = 6
# error