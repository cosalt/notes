class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def getsalary(self):
        return self.__salary
    
    def setsalary(self, num):
        self.__salary = num
    

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def giveraise(self, increase):
        temp = self.getsalary()
        self.setsalary(temp + increase)

manager1 = Manager("john", 200000)

print(manager1.getsalary())

manager1.giveraise(200000)

print(manager1.getsalary())

