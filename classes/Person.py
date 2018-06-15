from random import randrange

from Subject import Subject


class Person(object):
    def __init__(self):
        """
        Base class from which Student and Teacher are both drawn
        """
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')

    def determine_subject_proficiency(self):
        """
        Determine how well each teacher can teach each subject
        """
        subject = Subject()
        available_subjects = subject.subjects
        subject_proficiencies = dict()
        while len(available_subjects) > 0:
            this_subject = subject.get_subject(available_subjects)
            proficiency = subject.get_subject_proficiency()
            subject_proficiencies[this_subject] = proficiency

        return subject_proficiencies

    def get_initial(self):
        """
        Assign each teacher an initial
        :param teacher_number:
        """
        return self.alphabet[randrange(0, 23)]
