from pprint import pprint


from random import randrange

from Subject import Subject

class TeachingTime(object):
    def __init__(self):
        """
        This represents the amount of time during the day that the teacher has to teach their subject
        """

        self.subject = Subject()

        # Five hours
        self._total_time = 5
        self._time_per_subject = {}

    @property
    def time_per_subject(self):
        """
        The amount of time a teacher is able to spend on their subject with each class
        """
        return self._time_per_subject

    @time_per_subject.setter
    def time_per_subject(self, value):
        self._time_per_subject = value

    def assign_time_per_subject(self):
        """
        Assign the amount of time going to be spent on each subject
        """
        time_per_subject = {}
        while len(self.subject.subjects) > 0:
            this_subject = self.subject.get_subject(self.subject.subjects)
            subject_time = randrange(10, 500)
            time_per_subject[this_subject] = subject_time

        return time_per_subject
