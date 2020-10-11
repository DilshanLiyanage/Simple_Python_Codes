class Parent:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_data (self):
        print("Name is "+self.name+" and stays in "+self.address)


class Child(Parent):

    def childme (self):
        print("Child ,method")

child = Child("Tharusha", "Mathara")
child.display_data();
child.childme()
