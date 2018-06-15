from random import choice, randrange


class Subject(object):
    def __init__(self):
        """
        Subject on which a class can be based, and for which proficiency is determined for each student
        and teacher
        """
        self._subjects = ['math', 'science', 'reading', 'writing', 'history']

    @property
    def subjects(self):
        """
        Subjects available for teachers
        """
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        self._subjects = value

    def get_subject(self, available_subjects):
        """
        Get a random subject which has not already been assigned to another teacher\
        """
        assigned_subject = choice(available_subjects)
        available_subjects.remove(assigned_subject)
        return assigned_subject

    def get_subject_proficiency(self):
        """
        Determine how proficient a teacher is at teaching a given subject
        """
        return randrange(10, 100)
