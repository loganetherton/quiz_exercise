from TeachingTime import TeachingTime

class Class(object):
    def __init__(self):
        """
        Class will contain a single teacher and a number of students and quizzes. Teachers will educate
        students on the source material, assign quiz dates, administer quizzes, grade quizzes, and calculate
        final grades for students
        """

        # The amount of time the teacher has to teach the subject in any given day
        self.time_per_subject = None
        self.assign_classroom_time()

    def assign_classroom_time(self):
        teaching_time = TeachingTime()
        self.time_per_subject = teaching_time.assign_time_per_subject()