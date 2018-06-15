from Subject import Subject
from Person import Person


class Teachers(Person):
    def __init__(self):
        """
        Teachers will be assigned to a subject, generate quizzes, teach students on the subject material,
        and grade quizzes
        """
        super(Teachers, self).__init__()

        self.teachers = {}

    def generate_teachers(self):
        """
        Generate teachers for each subject
        """
        for i in range(5):
            self.teachers[i] = {'teacher_initial': self.get_initial()}
            # How effectively the teacher can teach each subject
            self.teachers[i]['proficiency'] = self.determine_subject_proficiency()
            # Subject the teacher will be teaching
            self.teachers[i]['subject'] = self.assign_subject()

        return self.teachers

    def assign_subject(self):
        """
        Assign a unique subject to each teacher
        """
        subject = Subject()
        assigned_subject = subject.get_subject(subject.subjects)
        return assigned_subject
