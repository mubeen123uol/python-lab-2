# Topic: Classes, Objects, and Instance Methods
# Advanced Back-End Development - Lecture 2

class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def show_info(self):
        print(f"My name is {self.name}, my roll number is {self.roll_no}, and I study {self.course}.")


if __name__ == '__main__':
    student1 = Student("Muhammad Mubeen", "70150831", "Advance Back-End Development")
    student2 = Student("Saad", "70154663", "Advance Back-End Development")
    student3 = Student("Sara", "70137363", "Advance Front-End Development")

    print("--- Student Information ---")
    student1.show_info()
    student2.show_info()
    student3.show_info()
