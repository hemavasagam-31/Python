class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40

student1 = Student("Rita", 78)
student1.show_details()
print("Passed:", student1.is_passed())
