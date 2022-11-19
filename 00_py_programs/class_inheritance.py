class Parent:
    '''
    This is parent class
    '''
    parent_count = 5
    def __init__(self):
        """
        This is "Parent" class constructor
        """
        print('Parent class contructor called')

    def parent_method(self):
        """
        This is parent class method
        """
        print('parent_method() called')

    def set_attr(self, count):
        '''
        This is count Set Function
        '''
        Parent.parent_count = count

    def get_attr(self):
        """
        This returns the count of parent class
        """
        print(Parent.parent_count)   

class Child(Parent):
    """
    This is child class
    """
    def __init__(self):
        """
        This is child class constructor method
        """
        print('Child class constructor called')
    
    def child_method(self):
        """
        This is child class method
        """
        print('child_method() called')

c = Child()
c.child_method()
print(c.parent_count)
c.parent_method()
c.set_attr(20)
c.get_attr()
print(c.parent_count)