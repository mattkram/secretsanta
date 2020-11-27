from random import random

partner = {'Matt': 'Amanda',
          'Tim': 'Meghan',
          'Kelly': None,
          'Marianne': 'Dillon'
         }

givers = [v for t in partner.iteritems() for v in t if v is not None]

while True:
    receivers = sorted(givers, key=lambda _: random())
    if all(g != r and
           r != partner.get(g, None) and
           g != partner.get(r, None) for g, r in zip(givers, receivers)):
        break

# Print results
for gr in zip(givers, receivers):
    print '{0} will give to {1}'.format(*gr)
    
