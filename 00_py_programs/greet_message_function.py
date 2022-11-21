def greet(name, msg):
    '''
    '''
    print('Hello {0}, {1}'.format(name, msg))

greet('Suresh', 'Good Morning')


def greet_good_morning(name, msg = 'Good Morning'):
    '''
    '''
    print('Hello {0}, {1}'.format(name, msg))

greet_good_morning('Suresh', 'Not that Way')