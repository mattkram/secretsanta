import random


def distribute_gifts(partners, last_year):
    # Flatten partner dictionary into a list of non-blank
    givers =  [person for pair in partners.items() for person in pair if person is not None]

    new_partners = dict(partners)
    for sibling, partner in partners.items():
        if partner is not None:
            new_partners[partner] = sibling
    partners = new_partners

    while True:
        receivers = sorted(givers, key=lambda _: random.random())
        g_r_dict = dict(zip(givers, receivers))

        if all(
            giver != receiver and
            receiver != partners.get(giver) and
            giver != partners.get(receiver) and
            receiver != last_year[giver] and
            g_r_dict[receiver] != giver
            for giver, receiver in g_r_dict.items()
        ):
            return zip(givers, receivers)

# Sibling: Partner
partner = {
    'Matt': 'Amanda',
    'Tim': 'Megan',
    'Kelly': 'Viral',
    'Marianne': None,
}

# Giver: Receiver
last_year = {
    'Matt': 'Tim',
    'Amanda': 'Kelly',
    'Marianne': 'Megan',
    'Megan': 'Marianne',
    'Tim': 'Viral',
    'Kelly': 'Amanda',
    'Viral': 'Matt',
}

results = distribute_gifts(partner, last_year)

for giver, receiver in results:
    print(giver, '->', receiver)
