class Person(object):
    def __init__(self, sex, forename, surname, age, location):
        self.sex = sex
        self.forename = forename
        self.surname = surname
        self.age = age
        self.location = location

    def name(self):
        return self.forename + " " + self.surname

    def display_person(self):
        print "Sex: %s" % self.sex
        print "Name: %s" % self.name()
        print "Age: %i" % self.age
        print "Location: %s" % self.location

    def birthday(self):
        self.age += 1


class Employee(Person):
    def __init__(self, sex, forename, surname, age, location, job, salary):
        Person.__init__(self, sex, forename, surname, age, location)
        self.job = job
        self.salary = salary

    def display_employee(self):
        self.display_person()
        print "Job: %s" % self.job
        print "Salary: %s" % unichr(163) + str(self.salary)

    def payrise(self):
        increase = 1.03
        self.salary *= increase


def main():
    a_person = Person('Male', 'Bill', 'Smith', 45, 'London')
    a_person.display_person()
    print
    a_employee = Employee('Male', 'John', 'Jones', 30, 'Liverpool', 'Stevedore', 25000)
    a_employee.display_employee()
    a_employee.payrise()
    a_employee.birthday()
    a_employee.display_employee()

main()
