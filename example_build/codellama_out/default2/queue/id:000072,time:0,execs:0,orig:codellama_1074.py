# using as to convert a set to a frozenset
s = {1, 2, 3}
f = s.as_frozenset()
print(f) # prints frozenset({1, 2, 3})

# using as to convert a frozenset to a set
fs = frozenset({1, 2, 3})
s = fs.as_set()
print(s) # prints {1, 2, 3}