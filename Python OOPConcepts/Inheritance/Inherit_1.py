'''Let's create a parent class: named Person, with firstname and lastname properties
and a printname method'''

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
# x = Person("Duhita", "Dharmadhikari")
# x.printname()

'''Now let's create a child class called as Student,
which will inherit the properties and methods from the Person class:'''

class Student(Person):
    
    '''If I give an __init__() function to the child student class
    then, Student will no longer inherit from Person'''
    
    '''To avoid that you can use def __init__(self, fname, lname):
                                    Person.__init__(self, fname, lname)
    In this way the Student class will continue to inherit from the Person class'''

# x = Student("Rohit", "Akole")
# x.printname()
    # def __init__(self, fname, lname):
    #     Person.__init__(self, fname, lname)
        
    '''Use Case 1: Super can be called upon in a single 
        inheritance, in order to refer to the parent class or
        multiple classes without explicitly naming them.
        It’s somewhat of a shortcut, but more importantly,
        it helps keep your code maintainable for the 
        foreseeable future.'''
        
    '''Use Case 2: Super can be called upon in a dynamic
        execution environment for multiple or collaborative
        inheritance. This use is considered exclusive to
        Python, because it’s not possible with languages 
        that only support single inheritance or are 
        statically compiled.'''

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",
               self.graduationyear)
        
