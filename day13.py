pairs, packets = [], [[[2]], [[6]]]
for p in open('input_d13.txt').read().split('\n\n'):
    a, b = map(eval, p.split('\n'))
    pairs.append((a, b))
    packets += [a, b]

print(packets)


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    elif a and b:
        q = compare(a[0], b[0])
        return q if q else compare(a[1:], b[1:])
    return 1 if a else (-1 if b else 0)


print(sum(i + 1 for i, x in enumerate(pairs) if compare(x[0], x[1]) == -1))

packets_sorted = sorted(packets, key=cmp_to_key(compare))
print((1 + packets_sorted.index([[2]])) * (1 + packets_sorted.index([[6]])))