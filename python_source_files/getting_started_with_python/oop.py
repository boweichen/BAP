"""
OOP
"""

class Staff():
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        
    def __repr__(self):
        return f'{self.name} works for {self.hours} hours'

class Firm():
    def __init__(self):
        self.staff_list = []

    def add_staff(self, staff):
        self.staff_list.append(staff)


#Instance
staff1 = Staff('Amy', 40)
staff2 = Staff('Tom', 35)
print(f'{staff1.name} works for {staff1.hours} hours.')

#Start firm
my_firm = Firm()
print(my_firm.staff_list)

#Add staff to list
my_firm.add_staff(staff1)
my_firm.add_staff(staff2)

#Show our list
print(my_firm.staff_list)
