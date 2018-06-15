from random import randrange

from Subject import Subject

class Quiz(object):
    def __init__(self):
        """
        Quiz will represent each individual quiz created and assigned by each teacher, handed out to students,
        graded, the results of which will be used to calculate final grades
        """

        self.quizzes = {}
        self.max_quizzes = 10

    def generate_quiz(self):
        """
        Generate 50 random quizzes on a variety of subjects and difficulties
        :return:
        """
        i = 0
        while i < self.max_quizzes:
            self.quizzes[i] = {'subject': self.determine_quiz_subject(), 'difficulty': self.determine_quiz_difficulty()}
            i = i + 1

        return self.quizzes

    def determine_quiz_subject(self):
        """
        The subject that the quiz will be covering
        """
        subject = Subject()
        return subject.get_subject(subject.subjects)


    def determine_quiz_difficulty(self):
        """
        the difficult of each quick
        """
        return randrange(10, 100)
        pass