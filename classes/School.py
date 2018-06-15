from random import randrange


class School(object):
    def __init__(self):
        """
        The shool class will handle the entirety of the interactions between the students and teachers, as well as
        determining the schoool year, assigning quizzes, grading quizzes, assigning final grades, and printing the
        results of each students' performance
        """

        self._school_year_length = None
        self.time_per_subject = None

    @property
    def school_year_length(self):
        """
        The number of days in the school year
        """
        return self._school_year_length

    @school_year_length.setter
    def school_year_length(self, value):
        self._school_year_length = value

    def determine_school_year_length(self):
        """
        Determine the number of days in a school year
        """
        self._school_year_length = randrange(50, 200)

    def assign_students_to_classes(self):
        """
        Randomly assign students to each class
        """
        pass
