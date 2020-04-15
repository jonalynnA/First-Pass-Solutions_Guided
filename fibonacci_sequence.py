'''RULES OF RECURSSION
1. Must have a base case.
2. Must change state toward the base case.
3. Must call itself, recursively.
'''


def fib(n, cache=None):
    print(n)
    print(cache)
    if cache is None:
        cache = {}
    # Base Case
    if n <= 2:
        return 1
    # Recursive call, should move towards base case
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        return answer


counter = 0


def foo(n):
    print(n)
    global counter
    counter += 1
    if n <= 1:
        return 1
    print(counter)
    return foo(n-1) + foo(n-1)


print(fib(10))
