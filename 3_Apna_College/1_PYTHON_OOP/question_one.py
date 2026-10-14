# class Student():
#     def __init__(self, name, maths, sci, eng):
#         self.name = name
#         self.maths = maths
#         self.sci = sci
#         self.eng = eng
#     def avg(self):
#         avg = 
#         print("Average Marks")

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello world")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average: ", sum/len(self.marks))

s1 = Student("Maulik", [90, 80, 99, 80])
s1.get_avg()
s1.hello()