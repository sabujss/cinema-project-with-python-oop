from manue import Manue
class Restuarent:
    def __init__(self,name):
        self.name=name
        self.employes=[]
        self.manue=Manue()

    def add_employe(self,employe):
        self.employes.append(employe)
        print(f'{employe.name} added successfully!!')

    def view_employe(self):
        print("Employee list here")
        for emp in self.employes:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.salary, emp.designation)

