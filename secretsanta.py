from random import random

     
class Person(object):
    """Represents a person as a simple data structure.

    Attributes
    ----------
    name: str
        Name of person
    email: str
        Email address
    partner: Person, optional, default=None
        The person's partner, who cannot receive a gift from this person
    gift_recipient: Person, default=None
        The person who will be receiving a gift from this person.
    """
    
    class Meta(type):
        """The Meta-class is used to allow indexing of the Person class by name"""    
        __all = []
        
        def append(cls, obj):
            cls.__all.append(obj)
            
        def __getitem__(cls, name):
            for o in cls.__all:
                if o.name == name:
                    return o
            return None

    __metaclass__ = Meta
        
    def __init__(self, name, email):
        Person.append(self)
        self.name = name
        self.email = email
        self._partner = None
        self.gift_recipient = None

    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Assign a parner to this person. Will also assign this person as the others' partner"""
        self._partner = partner
        partner._partner = self

    def __str__(self):
        s = ''
        s += '{0:10s} will give a gift to {1}'.format(self.name, self.gift_recipient.name)
        return s


def assign_secret_santa(people):
    """Randomly loops through each person in people. Assign a secret santa,
    checking that a person cannot give to themselves or to their partner.
    """
    
    finished = False
    while not finished:
        # Randomly sort the list of people, and designate as gift receivers
        # (people list is the list of givers)
        receivers = sorted(people, key=lambda _: random())
        print 'Givers:   ', [o.name for o in people]
        print 'Receivers:', [o.name for o in receivers]

        finished = True
        for giver, receiver in zip(people, receivers):
            if (giver.name == receiver.name or (giver.partner is not None and giver.partner.name == receiver.name)):
                print '{0} cannot give to {1}\n'.format(giver.name, receiver.name)
                finished = False
                break

        if finished is True:
            print 'Success!\n'

    for giver, receiver in zip(people, receivers):
        giver.gift_recipient = receiver

def main():
    # Create a list of all people
    people = [
        Person('Matt', 'matthew.robert.kramer@gmail.com'),
        Person('Amanda', 'acburriola@gmail.com'),
        Person('Tim', 'tim@gmail.com'),
        Person('Meghan', 'meghan@gmail.com'),
        Person('Kelly', 'kelly@gmail.com'),
        Person('Marianne', 'marianne@gmail.com'),
        Person('Dillon', 'dillon@mountain.com')
    ]

    # Assign partners (so they can't be each others' Santa
    Person['Matt'].partner = Person['Amanda']
    Person['Tim'].partner = Person['Meghan']
    Person['Marianne'].partner = Person['Dillon']

    # Assign the secret santa randomly
    assign_secret_santa(people)

    # Print results
    for person in people:
        print person
    
if __name__ == '__main__':
    main()
