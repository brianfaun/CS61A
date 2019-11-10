def reduce(f, s, initial):
    if s:
        return reduce(f, s[0:], f(initial, s[0]))
    else:
        return 1
