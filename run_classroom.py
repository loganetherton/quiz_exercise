from pprint import pprint

from classes import Quiz, Student, Teachers


class RunClassroom(object):
    """
    Main runner class for simulating students in a school environment
    """

    def __init__(self):
        self.teachers = {}
        self.students = {}
        self.quizzes = {}

        # Init the application
        self.generate_teachers()
        self.generate_students()
        self.create_quizzes()
        self.students_complete_quizzes()
        self.get_final_grades()
        self.display_student_performance()

    def generate_teachers(self):
        """
        Generate teachers and their abilities, which will affect the abilities of the students on the quizzes
        """
        teacher = Teachers()
        self.teachers = teacher.generate_teachers()

        # print('\033[44m' + '***********TEACHERS*************' + '\033[0m')
        # pprint(self.teachers)

    def generate_students(self):
        """
        Generate students, giving a level of ability in each subject
        """
        student = Student()
        self.students = student.generate_students()

        print('\033[44m' + '***********STUDENTS*************' + '\033[0m')
        pprint(self.students)

    def create_quizzes(self):
        """
        Generate the quizzes that the students will take, including subject and difficulty
        """
        quiz = Quiz()
        self.quizzes = quiz.generate_quiz()
        print('\033[44m' + '***********QUIZZeS*************' + '\033[0m')
        pprint(self.quizzes)

    def students_complete_quizzes(self):
        """
        Calculate quiz scores for each of the students who take each of the quizzes
        :return:
        """
        for key, quiz in self.quizzes.iteritems():
            quiz_subject = quiz['subject']
            quiz_difficulty = quiz['difficulty']
            for student_index, student_quiz in self.students.iteritems():
                subject_proficiency = student_quiz['proficiency'][quiz_subject]
                grade = (subject_proficiency + quiz_difficulty) / 2
                self.students[student_index]['subjects'][quiz_subject]['quiz_grades'].append(grade)
        pass

    def get_final_grades(self):
        """
        Calculate final grade for each subject for each student
        :return:
        """
        for student_index, student_final in self.students.iteritems():
            for grade_index, student_grade in student_final['subjects'].iteritems():
                # Sum test scores
                grade_this_subject = self.students[student_index]['subjects'][grade_index]
                quiz_sum = sum(student_grade['quiz_grades'])
                quiz_count_this_subject = len(grade_this_subject['quiz_grades'])

                grade_this_subject['final_grade'] = quiz_sum / quiz_count_this_subject if quiz_count_this_subject else 0

                # if quiz_count_this_subject:
                #     grade_this_subject['final_grade'] = quiz_sum / quiz_count_this_subject
                # else:
                #     grade_this_subject['final_grade'] = 0

        print('\033[44m' + '***********STUDENT QUIZ AND FINAL GRADES*************' + '\033[0m')
        pprint(self.students)

    def display_student_performance(self):
        pass


if __name__ == '__main__':
    classroom = RunClassroom()
