class Student:
    '''
    This is student class
    '''
    student_count = 0
    def __init__(self, name = None, subject = None, grade = None):
        '''
        This is constrctor method for student class
        '''
        self.name = name
        self.subject = subject
        self.grade = grade
        Student.student_count += 1

    def display_student_count(self):
        '''
        This method displays the total count of student
        '''
        print('Total number of students are: ' + str(Student.student_count))

    def display_student_information(self):
        '''
        This method dislays student's information
        '''
        try:
            print('\n\n\tName: {}\tSubject: {}\tGrade: {}\n\n'
            .format(self.name, self.subject, self. grade))
        except(AttributeError):
            
            if hasattr(self, 'name'):
                print('\n\n\tName: {}'.format(self.name), end='\n')
            else:
                print('\n\n\tName attribute missing.')
            
            if hasattr(self, 'subject'):
                print('\tSubject: {}'.format(self.subject))
            else:
                print('\tSubject attribute missing.')
            
            if hasattr(self, 'grade'):
                print('\tGrade: {}'.format(self.grade), '\n\n')
            else:
                print('\tGrade attribute missing.\n\n')

    def add_student(self):
        """
        This method takes input from user and adds new student
        """
        self.name = input('\tEnter student\'s name: ')
        self.subject = input('\tEnter subject: ')
        self.grade = input('\tEnter grade: ')
    
    def __del__(self):
        '''
        This is destructor method for student class
        '''
        class_name = self.__class__.__name__
        print(class_name, 'destroyed')

    
while True:
    try:
        print('\nUsage:\tq -- Quit\n\ta -- Add new studen\n\td -- Display last\n\tc -- Display count')
        choice = input("Enter your choice: ")
        i = 0
        if choice == 'q':
            break
        elif choice == 'a':
            student1 = Student()
            try:
                student1.add_student()
            except(KeyboardInterrupt):
                del student1
        elif choice == 'd':
            try:
                student1.display_student_information()
            except(NameError):
                print('Seems like we don\'t have any student enrolled yet.')
        elif choice == 'c':
            try:
                student1.display_student_count()
            except(NameError):
                print('Seems like we don\'t have any student enrolled yet.')
    except(KeyboardInterrupt):
        print('This is not the way to quit your program.\nPlese follow proper procedure.\tYou are not allowed to use Keyboard Interrupt')
