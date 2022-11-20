class Employee:
    '''
    This is employee class, this class contains all the information about employee handling
    Like employee count, employee name, employee age employee email only
    '''
    emp_count = 0
    
    def __init__(self, name, email = None, age = None):
        '''
        This is Constructor Method
        '''
        self.name =  name
        self.email = email
        self.age = age
        Employee.emp_count += 1
    
    def display_count(self):
        """
        This function prints the employee count
        """
        print('Total Employee Number is:', str(Employee.emp_count))

    def display_information(self):
        """
        This method prints the employee's information
        """
        print('Name:', self.name, '\nemail:', self.email, '\nAge:', self.age, '\n\n')
  
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print('Point ({}, {}) is created'.format(x, y))

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, 'destroyed')