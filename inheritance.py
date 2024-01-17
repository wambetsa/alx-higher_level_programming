"""class Person:
    #constructor
    def __init__(self, fname, lname, age, country):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
    def display(self):
        print(f"My name is: {self.lname} {self.fname}. I am {self.age} years old. I am {self.country}")
my_details = Person("Shitseswa", "Emmanuel", 26, "Kenyan")
my_details.display()

#creating child class - INHERITING FROM BASE/PARENT CLASS _ Person
class Nationality(Person):

    def print_nationality(self):
        print("National class called")
fulldetails = Person("Shitseswa", "Arthur", 30, "Australian")
fulldetails.display()

my_details = Nationality("Shitseswa", "Rebecca", 30, "English")
my_details.display()"""


"""#base/parent class
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

#child/derived class
class Employee(Person):
    def isEmployee(self):
        return True

employee = Person("Emmanuel Wambetsa")
print(employee.getName(), employee.isEmployee())

employee = Employee("Arthur Shitseswa")
print(employee.getName(), employee.isEmployee())"""


"""#parent class
class Person(object):
    #constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name
    #display method
    def display(self):
        print(self.id)
        print(self.name)

#derived/child class
class Employee(Person):
    def __init__(self, id, name, email, payroll_number):
        self.email = email
        self.payroll_number = payroll_number

        #call parent __init__ constructor
        Person.__init__(self, id, name)
#creation of an object variable or instance
a = Employee(3430710421, "Emmanuel Wambetsa Shitsewa", "wambetsae@gmail.com", 17133970)
#calling parent class using instance
a.display()"""


"""#parent/base class
class Person(object):
    #constructor of parent class
    def __init__(self, id, name):
        self.id = id
        self.name = name
    #print method
    def display(self):
        print(self.id)
        print(self.name)

#derived/child class
class Employee(Person):
    #constructor of derived/child class
    def __init__(self, id, name, email, phone):
        self.email = email
        self.phone = phone

        #invoke init constructor of the parent class
        Person.__init__(self, id, name)
a = Employee(34307304, "Emmanuel Wambetsa", "wambetsae@gmail.com", +254717133970)
a.display()"""


"""#use of super() built-in function to access parent methods and attributes in child class
#parent/base class
class Person(object):
    #parent/base class constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #display method
    def display(self):
        print(self.name, self.age)

#child/derived class
class Student(Person):
    #child/base class constructor
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        #inheriting parent class properties
        super().__init__("Arthur", age)
    
    #display infor method
    def displayInfor(self):
        print(self.sName, self.sAge)
#objects
a = Student("Emmanuel Wambetsa", 26)
a.display()
a.displayInfor()"""


"""#parent/base class
class Person(object):
    #constructor of parent/base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #display() method
    def display(self):
        print(self.name, self.age)
#child/derived class
class Student(Person):
    #base/child class constructor
    def __init__(self, name, age, dob, country):
        self.sName = name
        self.sAge = age
        self.dob = dob
        self.country = country
        #inherit parent properties
        super().__init__("Arthur Ochieng", age)
    #display_infor() function
    def display_infor(self):
        print(self.sName, self.sAge, self.dob, self.country)
a = Student("Emmanuel Wambetsa", 26, 1997, "Kenya")
a.display()
a.display_infor()"""


#base1 parent/base class
class Base1(object):
    #constructor of base/parent class
    def __init__(self):
        self.str1 = "Greek 1"
        print("Base 1")

"""#base2 parent/base class
class Base2(object):
    #constructor of base2 parent/base class
    def __init__(self):
        self.str2 = "Greek 2"
        print("Base 2")

#derived class from multiple parents
class Derived(Base1, Base2):
    #child/base class constructor
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived Child Class")
    #print strings
    def print_str(self):
        print(self.str1, self.str2)

#object
a = Derived()
a.print_str()"""


"""#MULTI_LEVEL INHERITANCE
class Base(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age
class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    def getAddress(self):
        return self.address

#object
a = GrandChild("Emmanuel Wambetsa", 26, "00100 Nairobi Kenya")
print(a.getName(), a.getAge(), a.getAddress())"""


"""#private members of the parent class
class C(object):
    def __init__(self):
        self.c = 21
        #private instance variable
        self.__d = 43
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
a = D()
print(a.c, a.__d)"""


class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)