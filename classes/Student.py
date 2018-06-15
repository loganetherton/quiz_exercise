from pprint import pprint

from Person import Person
from Subject import Subject


class Student(Person):
    def __init__(self):
        """
        Students will be assigned to classrooms, learn the quiz material, take quizzes, and be assigned a final
        grade for each class based on their quiz performance
        """
        super(Student, self).__init__()

        self.students = {}

    def generate_students(self):
        """
        Generate students for each subject
        """
        subject = Subject()
        subjects = subject.subjects
        # Create the student object to hold quiz grades amd final grades
        for i in range(50):
            self.students[i] = {'student_initial': self.get_initial()}
            # How effectively the student can learn each subject
            self.students[i]['proficiency'] = self.determine_subject_proficiency()
            self.students[i]['subjects'] = {}
            for subject in subjects:
                self.students[i]['subjects'][subject] = {'quiz_grades': [], 'final_grade': None}
        return self.students
