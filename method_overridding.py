class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def details(self):
        print("From Father class")

class Mother(Father):
    def __init__(self, father_name,mother_name):
        super().__init__(father_name)
        self.mother_name = mother_name

    def details(self):
        print("From mother class")

class Child(Mother):
    def __init__(self,father_name,mother_name, child_name):
        super().__init__(father_name,mother_name)
        self.child_name = child_name

    def show_child(self):
        print(f"Child: {self.child_name}")


child = Child("jhon","Jane","Emily")
child.details()