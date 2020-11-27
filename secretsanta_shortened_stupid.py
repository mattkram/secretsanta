import random

def f(p):
    h = [v for t in p.iteritems() for v in t if v != '']

    while 1:
        s = sorted(h, key=lambda _: random.random())
        if all(g != r and
               r != p.get(g, '') and
               g != p.get(r, '') for g, r in zip(h, s)):
            return zip(h, s)

# Print results
p = {'Matt': 'Amanda',
     'Tim': 'Meghan',
     'Kelly': '',
     'Marianne': 'Dillon'
    }

for g, r in f(p):
    print g, '->', r
