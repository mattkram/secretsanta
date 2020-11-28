import random


def distribute_gifts(sibling_partner_map, last_year):

    partners = dict(sibling_partner_map)
    for sibling, partner in sibling_partner_map.items():
        if partner is not None:
            partners[partner] = sibling

    givers = partners.keys()

    while True:
        receivers = sorted(givers, key=lambda _: random.random())
        g_r_dict = dict(zip(givers, receivers))

        if all(
            giver != receiver and                 # a person cannot give to themself
            receiver != partners.get(giver) and   # a person cannot give to their partner
            receiver not in last_year[giver] and  # a person cannot give to the same person as in the last however many years
            g_r_dict[receiver] != giver           # two people cannot give to each other
            for giver, receiver in g_r_dict.items()
        ):
            return g_r_dict

# Sibling: Partner
partner = {
    'Matt': 'Amanda',
    'Tim': 'Megan',
    'Kelly': 'Viral',
    'Marianne': None,
}

# Giver: Receiver
last_year = {
    'Matt': ['Tim'],
    'Amanda': ['Kelly'],
    'Marianne': ['Megan'],
    'Megan': ['Marianne'],
    'Tim': ['Viral'],
    'Kelly': ['Amanda'],
    'Viral': ['Matt'],
}

results = distribute_gifts(partner, last_year)

for giver, receiver in results.items():
    print(giver, '->', receiver)
