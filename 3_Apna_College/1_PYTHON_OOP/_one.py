class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        print("Adding New Student in Database.")
    def welcome(self):
        print("Welcome ", self.full_name)
s1 = Student("Maulik Darji")
s1.welcome()