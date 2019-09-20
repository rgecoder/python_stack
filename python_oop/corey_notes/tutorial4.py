# Python OOP - Inheritance: Creating Subclasses


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # pass first,last,pay to our employees init method, let that class handle arguments, DRY
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

        # alternative way
        # Employee.__init__(self, first,last,pay)

    # by chaging raise_amt in subclass, it does not change raise_amt in other instances


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): # pass in a list
        # pass first,last,pay to our employees init method, let that class handle arguments, DRY
        super().__init__(first, last, pay)
        if employees is None:  # never want to pass mutable datatypes as default arg i.e. list dict
            self.employee = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
      for emp in self.employees:
        print('-->', emp.fullname())    


# first look at developer class for init method, if empty will walk up chain of inheritance (METHOD RESOLUTION ORDER)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Employee('Test', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)

# print(help(Developer))
# VERY USEFUL

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)

mgr_1.remove_emp(dev_1)


mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))

